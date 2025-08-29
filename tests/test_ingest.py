import os
from src.ingest import ingest_data

def test_ingest_creates_json_file():
    path = ingest_data(days=1)
    assert os.path.exists(path), f"File not found: {path}"
    assert path.endswith('.json'), "Ingested file is not a JSON file"
