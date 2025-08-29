import sqlite3
import pandas as pd
from src.load import load_to_sqlite, TABLE_NAME

def test_load_to_sqlite_inserts_data(tmp_path):
    test_csv = tmp_path / "test_data.csv"
    test_db = tmp_path / "test_db.sqlite"

    df = pd.DataFrame({
        "time_tag": ["2025-08-05T00:00:00Z"],
        "satellite": [1],
        "flux": [0.1],
        "observed_flux": [0.1],
        "electron_correction": [0.0],
        "electron_contamination": [0.0],
        "energy": ["0.1-0.8nm"]
    })
    df.to_csv(test_csv, index=False)

    load_to_sqlite(str(test_csv), str(test_db))

    conn = sqlite3.connect(test_db)
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
    count = cursor.fetchone()[0]
    conn.close()

    assert count == 1, "Expected 1 row inserted into the database"
