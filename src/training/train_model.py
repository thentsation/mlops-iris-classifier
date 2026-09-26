import pandas as pd
from sklearn.base import ClassifierMixin
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from utils.metrics import Metrics


class ModelTrainer:
    def __init__(self, model: ClassifierMixin | None = None) -> None:
        self.model = model or RandomForestClassifier(n_estimators=100, random_state=42)

    def train(self, X: pd.DataFrame, y: pd.Series) -> tuple[ClassifierMixin, float]:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        accuracy = Metrics.calculate_accuracy(y_test, y_pred)
        return self.model, accuracy
