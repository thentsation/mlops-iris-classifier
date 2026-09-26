from sklearn.datasets import load_iris

from training.train_model import ModelTrainer


def test_train_returns_fitted_model_and_reasonable_accuracy() -> None:
    iris = load_iris(as_frame=True)
    X, y = iris.data, iris.target

    trainer = ModelTrainer()
    model, accuracy = trainer.train(X, y)

    assert accuracy > 0.8
    assert model.predict(X.iloc[:1]).shape == (1,)
