import sqlite3
import pandas as pd
from src.config import DB_FILENAME

def query_db(query):
    conn = sqlite3.connect(DB_FILENAME)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows

def load_to_sqlite(filepath: str, db_filepath: str = "data/processed/solar_storm_data.sqlite"):

    conn = sqlite3.connect(db_filepath)
    df = pd.read_csv(filepath)
    df.to_sql("solar_storm_data", conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()
