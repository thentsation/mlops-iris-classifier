from config.config import Config
from data.data_loader import DataLoader
from registry.model_registry import ModelRegistry
from training.train_model import ModelTrainer


def main() -> float:
    loader = DataLoader(Config.DATA_PATH)
    df = loader.load_data()
    X = df.drop("target", axis=1)
    y = df["target"]

    trainer = ModelTrainer()
    model, accuracy = trainer.train(X, y)

    ModelRegistry.log_model_mlflow(
        model,
        Config.EXPERIMENT_NAME,
        params={"n_estimators": Config.N_ESTIMATORS},
        metrics={"accuracy": accuracy},
    )
    ModelRegistry.save_model_bentoml(model, Config.MODEL_NAME)

    print(f"Model trained and saved. Accuracy: {accuracy}")
    return accuracy


if __name__ == "__main__":
    main()
