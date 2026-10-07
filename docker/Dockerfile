FROM python:3.12-slim AS builder

WORKDIR /app

COPY config/requirements.lock ./config/

RUN pip install --no-cache-dir --prefix=/install -r ./config/requirements.lock

FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

COPY --from=builder /install /usr/local
RUN pip install --no-cache-dir --upgrade setuptools

COPY src ./src
COPY data/iris.csv ./data/iris.csv

RUN MLFLOW_DISABLE_AGENT_HINT=1 PYTHONPATH=/app/src python src/main.py

RUN useradd --create-home appuser
USER appuser

ENV PYTHONPATH=/app/src

EXPOSE 3000

CMD ["bentoml", "serve", "src.serving.iris_service:IrisClassifierService", "--production", "--host", "0.0.0.0", "--port", "3000"]
