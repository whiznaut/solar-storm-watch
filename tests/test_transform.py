import os
import pandas as pd
from src.transform import transform_data

def test_transform_creates_csv_file():
    input_path = "data/raw/sample_test_input.json"

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
