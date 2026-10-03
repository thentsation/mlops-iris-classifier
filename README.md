# Iris Classifier MLOps Project

> Leia em [português](README.pt-br.md).

An end-to-end MLOps example for an Iris classifier: [DVC](https://dvc.org/) for data versioning, [MLflow](https://mlflow.org/) for experiment tracking, and [BentoML](https://www.bentoml.com/) for model serving, on top of scikit-learn.

An in-depth write-up of the productization of this project — including a broken DVC remote that never actually worked — is available in [ARTIGO.md](ARTIGO.md) (pt-br) / [ARTIGO.en-us.md](ARTIGO.en-us.md) (en-us).

## Project structure

```text
src/
├── config/config.py            # Config (data path, model name, experiment name)
├── data/data_loader.py          # reads the already-`dvc pull`ed local CSV
├── training/train_model.py       # RandomForestClassifier + train/test split + accuracy
├── registry/model_registry.py    # logs to MLflow, saves to the BentoML model store
├── serving/iris_service.py        # IrisClassifier (plain, DI-friendly) + IrisClassifierService (@bentoml.service wrapper)
└── main.py                        # load -> train -> log (MLflow) -> save (BentoML)
```

## Getting started

```bash
make install    # creates .venv and installs deps
make data       # dvc pull - materializes data/iris.csv from the local DVC remote
make train      # trains the model, logs to MLflow, saves it to the BentoML model store
make serve      # bentoml serve --reload
```

- Swagger UI: http://localhost:3000/docs
- API endpoint: `POST http://localhost:3000/classify`
- MLflow UI: `.venv/bin/mlflow ui` (reads `./mlruns`, gitignored, generated locally by `make train`)

Run with Docker instead (the image trains the model at build time, from the CSV already pulled by CI/you):

```bash
make docker-build
make docker-run
```

## Development

```bash
make test        # pytest
make coverage     # pytest with coverage report
make lint         # ruff check
make format       # ruff format
make typecheck    # mypy
```

CI and deploy run on the platform's Jenkins (`Jenkinsfile` → `appPipeline` from the `platform` Shared Library, repo devops-platform), triggered by webhooks; there are no GitHub Actions.

- **PRs and branches** — contract validation; `docker build --target test` (`ruff check`, `ruff format --check`, `mypy`, `pytest` with ≥90% coverage on Python 3.11 and 3.12, tool versions from `config/requirements-dev.txt`); `pip-audit` on `config/requirements.lock`; Trivy (CRITICAL/HIGH) on the runtime image.
- **main** — all of the above, then build, smoke test, push to OCIR, deploy behind Traefik at https://mlops-iris.137-131-175-7.sslip.io with automatic rollback, release with python-semantic-release (version, CHANGELOG, tag and GitHub release) and a rebuild of the portfolio. Also rebuilt every Monday to pick up security patches.
- **Dependencies** — Renovate (Jenkins job `platform/renovate`, `renovate.json` → devops-platform preset): daily updates, weekly lockfile maintenance, Dependency Dashboard issue and auto-merge of patch/minor after Jenkins passes.

## Data versioning with DVC

`data/iris.csv` is DVC-tracked (`data/iris.csv.dvc`), backed by a **local, git-committed remote** (`.dvc-storage/`) instead of a cloud bucket — this keeps the example fully self-contained: `dvc pull` works right after `git clone`, with no cloud credentials to configure. Swap the remote (`dvc remote modify storage url s3://...`) for a real deployment.
