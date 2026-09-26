from typing import Any

import mlflow
import mlflow.sklearn
from sklearn.base import ClassifierMixin

import bentoml


class ModelRegistry:
    @staticmethod
    def log_model_mlflow(
        model: ClassifierMixin,
        experiment_name: str,
        params: dict[str, Any],
        metrics: dict[str, float],
    ) -> None:
        mlflow.set_experiment(experiment_name)
        with mlflow.start_run():
            mlflow.log_params(params)
            mlflow.log_metrics(metrics)
            mlflow.sklearn.log_model(
                model, name="model", skops_trusted_types=["sklearn.tree._tree.Tree"]
            )

    @staticmethod
    def save_model_bentoml(model: ClassifierMixin, model_name: str) -> bentoml.Model:
        return bentoml.sklearn.save_model(model_name, model)
