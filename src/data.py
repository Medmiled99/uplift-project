"""Load the Criteo uplift dataset (v2.1, the unbiased version)."""
import os
from pathlib import Path

import pandas as pd

FEATURES = [f"f{i}" for i in range(12)]
OUTCOMES = ["visit", "conversion"]
EXPECTED_ROWS = 13_979_592

DATA_DIR = Path(os.environ.get("CRITEO_DATA_DIR", Path.home() / "data" / "criteo-uplift"))
CSV_PATH = DATA_DIR / "criteo-uplift-v2.1.csv.gz"
PARQUET_PATH = DATA_DIR / "criteo-uplift-v2.1.parquet"

DTYPES = {
    **{col: "float32" for col in FEATURES},
    "treatment": "int8",
    "conversion": "int8",
    "visit": "int8",
    "exposure": "int8",
}


def load_criteo(sample_frac=None, seed=42):
    """Return the dataset, optionally as a random sample for quick work.

    The first call reads the CSV (about a minute) and saves a parquet copy, so
    later calls are much faster.
    """
    if PARQUET_PATH.exists():
        df = pd.read_parquet(PARQUET_PATH)
    else:
        if not CSV_PATH.exists():
            raise FileNotFoundError(f"{CSV_PATH} not found. See the README for the download link.")
        df = pd.read_csv(CSV_PATH, dtype=DTYPES)
        if len(df) != EXPECTED_ROWS:
            raise ValueError(f"Expected {EXPECTED_ROWS:,} rows, got {len(df):,}. The file may be incomplete.")
        df.to_parquet(PARQUET_PATH, index=False)

    if sample_frac is not None:
        df = df.sample(frac=sample_frac, random_state=seed).reset_index(drop=True)
    return df
