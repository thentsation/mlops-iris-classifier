from unittest.mock import patch

import pandas as pd

import main as main_module


def test_main_trains_logs_and_saves() -> None:
    df = pd.DataFrame(
        {
            "sepal_length": [5.1, 4.9, 6.7, 6.3],
            "target": [0, 0, 1, 1],
        }
    )

    with (
        patch.object(main_module.DataLoader, "load_data", return_value=df),
        patch.object(main_module.ModelRegistry, "log_model_mlflow") as log_mlflow,
        patch.object(main_module.ModelRegistry, "save_model_bentoml") as save_bentoml,
    ):
        accuracy = main_module.main()

    assert 0.0 <= accuracy <= 1.0
    log_mlflow.assert_called_once()
    save_bentoml.assert_called_once()
