from data.data_loader import DataLoader


def test_load_data_reads_local_csv(tmp_path) -> None:
    csv_path = tmp_path / "iris.csv"
    csv_path.write_text("sepal_length,target\n5.1,0\n4.9,0\n")

    df = DataLoader(str(csv_path)).load_data()

    assert list(df.columns) == ["sepal_length", "target"]
    assert len(df) == 2
