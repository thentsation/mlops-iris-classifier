from unittest.mock import MagicMock, patch

from registry.model_registry import ModelRegistry


def test_log_model_mlflow_logs_params_and_metrics() -> None:
    model = MagicMock()

    with patch("registry.model_registry.mlflow") as mlflow_mock:
        mlflow_mock.start_run.return_value.__enter__ = MagicMock()
        mlflow_mock.start_run.return_value.__exit__ = MagicMock(return_value=False)

        ModelRegistry.log_model_mlflow(
            model,
            "iris_classification",
            params={"n_estimators": 100},
            metrics={"accuracy": 0.97},
        )

    mlflow_mock.set_experiment.assert_called_once_with("iris_classification")
    mlflow_mock.log_params.assert_called_once_with({"n_estimators": 100})
    mlflow_mock.log_metrics.assert_called_once_with({"accuracy": 0.97})
    mlflow_mock.sklearn.log_model.assert_called_once()


def test_save_model_bentoml_delegates_to_bentoml_sklearn() -> None:
    model = MagicMock()

    with patch("registry.model_registry.bentoml") as bentoml_mock:
        ModelRegistry.save_model_bentoml(model, "iris_classifier")

    bentoml_mock.sklearn.save_model.assert_called_once_with("iris_classifier", model)
