import os
import json
import pandas as pd
from datetime import datetime
from src.config import RAW_DIR, PROCESSED_DIR

def transform_data(filepath):
    print(f"[INFO] Transforming data from: {filepath}")

    with open(filepath, "r") as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    df['time_tag'] = pd.to_datetime(df['time_tag'])

    df = df.dropna()

    df = df.drop_duplicates(subset='time_tag')

    os.makedirs(PROCESSED_DIR, exist_ok=True)

    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")
    filename = f"xrays_1day_clean_{timestamp}.csv"
    output_path = os.path.join(PROCESSED_DIR, filename)

    df.to_csv(output_path, index=False)
    print(f"[INFO] Transformed data saved to: {output_path}")

    return output_path
