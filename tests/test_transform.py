import os
import pandas as pd
import json
from src.transform import transform_data

def test_transform_creates_csv_file(tmp_path):
    input_path = tmp_path / "sample_test_input.json"

    with open(input_path, "w") as f:
        json.dump([
            {
                "time_tag": "2025-01-01T00:00:00Z",
                "satellite": "GOES-16",
                "flux": 42.0,
                "observed_flux": 41.5,
                "electron_correction": 0.1,
                "electron_contamination": 0.05,
                "energy": "0.1-0.8nm"
            }
        ], f)

    assert os.path.exists(input_path), f"Missing test input file: {input_path}"

    output_path = transform_data(input_path)
    assert os.path.exists(output_path), f"Output file not created: {output_path}"
    assert output_path.endswith(".csv"), "Transformed file is not a CSV"

    df = pd.read_csv(output_path)
    assert not df.empty, "Transformed CSV is empty"

    expected_columns = [
        "time_tag", "satellite", "flux", "observed_flux",
        "electron_correction", "electron_contamination", "energy"
    ]
    for col in expected_columns:
        assert col in df.columns, f"Missing column: {col}"
