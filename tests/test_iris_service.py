import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

from serving.iris_service import IrisClassifier


def _trained_model() -> RandomForestClassifier:
    iris = load_iris()
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(iris.data, iris.target)
    return model


def test_classify_reshapes_1d_input() -> None:
    classifier = IrisClassifier(model=_trained_model())
    result = classifier.classify(np.array([5.1, 3.5, 1.4, 0.2]))
    assert result.shape == (1,)


def test_classify_accepts_2d_input() -> None:
    classifier = IrisClassifier(model=_trained_model())
    result = classifier.classify(np.array([[5.1, 3.5, 1.4, 0.2], [6.7, 3.0, 5.2, 2.3]]))
    assert result.shape == (2,)
