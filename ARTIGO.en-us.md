[🇧🇷 Português](ARTIGO.md) | 🇺🇸 English

# The DVC that never pulled a single byte

This project sells itself as "real MLOps": DVC for data, MLflow for experiments, BentoML for serving. Three real pieces. The problem is one of them never actually worked — the DVC remote pointed at `/home/ntsation/docs/mlops-iris-classifier/dvc`, an absolute path on the old machine where the project was created. `dvc pull` anywhere else (including CI, including a fresh clone) either failed silently or never ran, because nobody had ever tested the flow from a clean checkout.

## What I had

A duplicated structure — part of the code in `src/` (SOLID `data`, `training`, `registry`, `utils` layers), and part loose at the root (`services/iris_services.py`, `train.py`, `config/`) surviving from an unfinished migration. A 0-byte `models/models.pkl`. Committed `.pyc` bytecode (`src/__pycache__/`). A `bentofile.yaml` pointing at `src.serve:svc`, a module that doesn't exist. And the BentoML service on the old API (`bentoml.io.NumpyNdarray`, `Service(...)`), while the other projects in the org already use the `@bentoml.service` decorator.

## Fixing DVC for real, not just cosmetically

I reconfigured the remote to a local directory **versioned in git itself** (`.dvc-storage/`), regenerated `data/iris.csv` from scikit-learn's bundled dataset (the original CSV was never committed — only the `.dvc` pointer, with the real blob nowhere to be found), ran `dvc add` + `dvc push`, and tested the full cycle: delete `data/iris.csv`, run `dvc pull`, confirm it comes back. It's self-contained now — clone the repo, `dvc pull` works, no cloud credentials needed.

```text
$ rm data/iris.csv && dvc pull
A       data/iris.csv
1 file added
```

## A decision I reversed midway through

My first version of `DataLoader` kept `dvc.api.get_url()` — resolving the data's URL through DVC's API before reading it with pandas. Made sense in my head: "that's how you use DVC." But when I packaged training into Docker, it broke: `dvc.api.get_url()` requires a working git repository, and the final image has no `.git` (I deliberately only copy `src/` and the already-materialized CSV, to keep the image small).

I stopped to think about the actual flow: the whole pipeline already runs `dvc pull` **before** training (in `make train`, in CI, in the step preceding the image build) — by that point the file is already on disk, materialized. Calling `dvc.api.get_url()` again inside the Python code was redundant, and worse, it's what was breaking Docker. `DataLoader` became a plain `pd.read_csv()`:

```python
class DataLoader:
    def __init__(self, data_path: str) -> None:
        self.data_path = data_path

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.data_path)
```

DVC still does its job — versioning and materializing the data — just outside the training code, where it belongs.

## Modernizing the BentoML service, and finding an import bug only after actually running it

I rewrote the service in the `@bentoml.service` pattern (same as `iris-classification-bentoml`), splitting `IrisClassifier` (plain, model injected, testable without the BentoML runtime) from the decorated wrapper. mypy and the tests passed on the first try. What only showed up once I actually ran the container and hit the endpoint: `bentoml serve src.serving.iris_service:IrisClassifierService` failed with `No module named 'config'`.

The cause: `bentoml serve <module>` imports the service by dotted path from the working directory (`/app` is on the path, so `src.serving...` resolves) — but the code inside the module does `from config.config import Config`, a bare import that only resolves if `/app/src` is **also** on the path. Running `python src/main.py` works without any extra configuration because Python already puts the script's own directory (`/app/src`) on `sys.path`; `bentoml serve` doesn't do you that favor. `ENV PYTHONPATH=/app/src` was missing from the Dockerfile — and this exact bug was already sitting, unnoticed, in `iris-classification-bentoml`, published two days earlier. I fixed both.

## The rest of the pattern

Full CI (ruff, pytest with a 90% floor, mypy, pip-audit, Docker+Trivy+GHCR, dependabot, semantic release), with one adjustment: the CI's Docker job runs `dvc pull` before the build, since the image expects `data/iris.csv` already materialized in the build context. `pip-audit` came out clean after swapping the original `requirements.txt`'s archaeological pins (BentoML 1.0.15, MLflow 2.3.1, scikit-learn 1.2.2, pandas 1.5.3 — all from 2023) for current ones, and after silencing one CVE with no published fix in `diskcache` (a transitive dependency of `dvc-data` that uses pickle for its local cache — exploiting it requires write access to the cache directory, meaning whoever could exploit it would already have full access to the machine).
