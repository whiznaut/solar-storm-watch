import os
import requests
from datetime import datetime, timedelta
from src.config import RAW_DIR

BASE_URL = "https://services.swpc.noaa.gov/json/goes/primary/xrays-1-day.json"

def fetch_xray_data():
    print("[INFO] Fetching X-ray data...")
    response = requests.get(BASE_URL)
    response.raise_for_status()
    return response.json()

def save_raw_data(data, days):
    os.makedirs(RAW_DIR, exist_ok=True)

    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")
    filename = f"xrays_1day_{timestamp}.json"
    filepath = os.path.join(RAW_DIR, filename)

    with open(filepath, "w") as f:
        import json
        json.dump(data, f, indent=2)

    print(f"[INFO] Raw data saved to {filepath}")
    return filepath

def ingest_data(days=1):
    data = fetch_xray_data()
    return save_raw_data(data, days)
