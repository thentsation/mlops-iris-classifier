import numpy as np
from sklearn.metrics import accuracy_score


class Metrics:
    @staticmethod
    def calculate_accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
        return float(accuracy_score(y_true, y_pred))
