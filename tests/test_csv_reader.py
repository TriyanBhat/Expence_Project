from app.ingestion.csv_reader import read_csv_files

def test_csv_reader():
    rows = read_csv_files("data")
    assert isinstance(rows, list)
    assert len(rows) > 0