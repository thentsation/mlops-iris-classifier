import pandas as pd


class DataLoader:
    """Reads a local file that's already been `dvc pull`ed (see the `data` Makefile target)."""

    def __init__(self, data_path: str) -> None:
        self.data_path = data_path

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.data_path)
