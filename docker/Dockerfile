FROM python:3.12-slim AS builder

WORKDIR /app

COPY config/requirements.lock ./config/

RUN pip install --no-cache-dir --prefix=/install -r ./config/requirements.lock

# CI (o Jenkins roda docker build --target test): ruff, mypy e pytest com cobertura
# mínima de 90% em Python 3.11 e 3.12, nas versões fixadas em config/requirements-dev.txt
# (atualizadas pelo Renovate). pip-audit e Trivy rodam no pipeline da plataforma, fora do
# cache de build, porque o resultado muda com as bases de vulnerabilidades.
FROM python:3.12-slim AS lint

WORKDIR /app

COPY config/requirements.txt config/requirements-dev.txt ./config/

RUN pip install --no-cache-dir -r ./config/requirements.txt \
    $(grep -E '^(ruff|mypy)==' ./config/requirements-dev.txt)

COPY . .

RUN ruff check . && ruff format --check . && mypy && touch /ok

FROM python:3.11-slim AS pytest-py311

WORKDIR /app

COPY config/requirements.txt config/requirements-dev.txt ./config/

RUN pip install --no-cache-dir -r ./config/requirements.txt \
    $(grep -E '^(pytest|pytest-cov)==' ./config/requirements-dev.txt)

COPY . .

RUN pytest --cov=src --cov-report=term-missing --cov-fail-under=90 && touch /ok

FROM python:3.12-slim AS pytest-py312

WORKDIR /app

COPY config/requirements.txt config/requirements-dev.txt ./config/

RUN pip install --no-cache-dir -r ./config/requirements.txt \
    $(grep -E '^(pytest|pytest-cov)==' ./config/requirements-dev.txt)

COPY . .

RUN pytest --cov=src --cov-report=term-missing --cov-fail-under=90 && touch /ok

FROM scratch AS test

COPY --from=lint /ok /lint.ok
COPY --from=pytest-py311 /ok /pytest-py311.ok
COPY --from=pytest-py312 /ok /pytest-py312.ok

# data/iris.csv é versionado pelo DVC, com o remote local .dvc-storage/ dentro do repo:
# equivale a um dvc pull, conferindo o md5 registrado em data/iris.csv.dvc.
FROM python:3.12-slim AS data

WORKDIR /app

COPY data/iris.csv.dvc ./data/
COPY .dvc-storage ./.dvc-storage

RUN md5=$(sed -n 's/^- md5: //p' data/iris.csv.dvc) \
    && cp ".dvc-storage/files/md5/$(echo "$md5" | cut -c1-2)/$(echo "$md5" | cut -c3-)" data/iris.csv \
    && echo "$md5  data/iris.csv" | md5sum -c -

FROM python:3.12-slim AS runtime

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

COPY --from=builder /install /usr/local
RUN pip install --no-cache-dir --upgrade setuptools

# O modelo é treinado no build (como root) e servido como appuser: o store do BentoML
# precisa ficar num caminho fixo, fora do HOME de cada usuário.
ENV BENTOML_HOME=/opt/bentoml

COPY src ./src
COPY --from=data /app/data/iris.csv ./data/iris.csv

RUN MLFLOW_DISABLE_AGENT_HINT=1 PYTHONPATH=/app/src python src/main.py && chmod -R a+rX "$BENTOML_HOME"

RUN useradd --create-home appuser
USER appuser

ARG APP_VERSION=dev
ENV APP_VERSION=$APP_VERSION

ENV PYTHONPATH=/app/src

EXPOSE 3000

CMD ["bentoml", "serve", "src.serving.iris_service:IrisClassifierService", "--production", "--host", "0.0.0.0", "--port", "3000"]

HEALTHCHECK --interval=30s --timeout=5s --start-period=60s --retries=3 \
    CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:3000/healthz', timeout=4)"]
