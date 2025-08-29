
import argparse
import logging
from datetime import datetime
from src.ingest import ingest_data
from src.transform import transform_data
from src.load import load_to_sqlite

def main(days: int):
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(message)s"
    )

    logging.info(f"Starting ETL pipeline for the last {days} day(s)...")

    raw_file = ingest_data(days=days)

    processed_file = transform_data(raw_file)

    load_to_sqlite(processed_file)

    logging.info("ETL pipeline completed successfully at %s", datetime.now().isoformat())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solar Storm Watch ETL Pipeline")
    parser.add_argument("--days", type=int, default=1, help="Number of past days to fetch data for")
    args = parser.parse_args()

    main(args.days)