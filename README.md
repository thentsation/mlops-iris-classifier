# Iris Classifier MLOps Project

[![Python CI](https://github.com/thentsation/mlops-iris-classifier/actions/workflows/pipeline_python.yaml/badge.svg)](https://github.com/thentsation/mlops-iris-classifier/actions/workflows/pipeline_python.yaml)
[![Docker CI/CD](https://github.com/thentsation/mlops-iris-classifier/actions/workflows/pipeline_docker.yaml/badge.svg)](https://github.com/thentsation/mlops-iris-classifier/actions/workflows/pipeline_docker.yaml)

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

CI runs ruff, pytest (coverage gate), mypy and pip-audit on every push/PR, plus a scheduled daily run. Docker images are built (after `dvc pull`), scanned with Trivy, and published to GHCR on `main`. Dependabot keeps pip, the Docker base image, and GitHub Actions up to date, with patch/minor bumps auto-merged. Releases are tagged automatically with [python-semantic-release](https://python-semantic-release.readthedocs.io/).

## Data versioning with DVC

`data/iris.csv` is DVC-tracked (`data/iris.csv.dvc`), backed by a **local, git-committed remote** (`.dvc-storage/`) instead of a cloud bucket — this keeps the example fully self-contained: `dvc pull` works right after `git clone`, with no cloud credentials to configure. Swap the remote (`dvc remote modify storage url s3://...`) for a real deployment.
