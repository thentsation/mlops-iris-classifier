import numpy as np
from sklearn.base import ClassifierMixin

import bentoml
from config.config import Config


class IrisClassifier:
    """Plain, framework-free classifier used both by the API layer and by tests."""

    def __init__(self, model: ClassifierMixin | None = None) -> None:
        self.model = model or bentoml.sklearn.load_model(f"{Config.MODEL_NAME}:latest")

    def classify(self, input_data: np.ndarray) -> np.ndarray:
        if input_data.ndim == 1:
            input_data = input_data.reshape(1, -1)
        return self.model.predict(input_data)


@bentoml.service(
    resources={
        "cpu": "1",
        "memory": "1Gi",
    },
)
class IrisClassifierService:
    def __init__(self) -> None:
        self._classifier = IrisClassifier()

    @bentoml.api
    def classify(self, input_series: np.ndarray) -> np.ndarray:
        return self._classifier.classify(input_series)
