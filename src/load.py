import sqlite3
import pandas as pd
from pathlib import Path
import os
from datetime import datetime
from src.config import PROCESSED_DIR, DB_FILENAME

TABLE_NAME = "xray_flares"

def load_to_sqlite(csv_file: Path, db_path: Path = DB_FILENAME):
    print(f"[INFO] Loading data from: {csv_file}")

    df = pd.read_csv(csv_file)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            time_tag TEXT PRIMARY KEY,
            satellite INTEGER,
            flux REAL,
            observed_flux REAL,
            electron_correction REAL,
            electron_contamination REAL,
            energy TEXT
        )
    ''')

    insert_query = f'''
        INSERT OR IGNORE INTO {TABLE_NAME} (
            time_tag, satellite, flux, observed_flux,
            electron_correction, electron_contamination, energy
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    '''

    data = df.to_records(index=False)
    cursor.executemany(insert_query, data)

    inserted = cursor.rowcount
    print(f"[INFO] Inserted {inserted} new rows (duplicates ignored).")

    conn.commit()
    conn.close()



def get_latest_processed_file():
    files = sorted([
        f for f in os.listdir(PROCESSED_DIR)
        if f.endswith(".csv")
    ], reverse=True)

    return os.path.join(PROCESSED_DIR, files[0]) if files else None


def main():
    latest_file = get_latest_processed_file()
    if latest_file:
        load_to_sqlite(latest_file)
    else:
        print("[ERROR] No processed file found to load.")

if __name__ == "__main__":
    main()