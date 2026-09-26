import numpy as np

from utils.metrics import Metrics


def test_calculate_accuracy_all_correct() -> None:
    y_true = np.array([0, 1, 2, 1])
    assert Metrics.calculate_accuracy(y_true, y_true) == 1.0


def test_calculate_accuracy_partial() -> None:
    y_true = np.array([0, 1, 1, 1])
    y_pred = np.array([0, 1, 0, 0])
    assert Metrics.calculate_accuracy(y_true, y_pred) == 0.5
