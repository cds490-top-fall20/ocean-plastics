import mlw.mlw_pipeline
import mdmap.mdmap_pipeline
import mdt.mdt_pipeline

import os
import pandas as pd

DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data"
    )
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")
OUTPUT_DIR = os.path.join(DATA_DIR, "final")

df = pd.concat(
        (
            pd.read_csv(os.path.join(PROCESSED_DIR, f)) 
            for f in os.listdir(PROCESSED_DIR) 
            if f[-4:] == ".csv"
        )
    )

df.to_csv(
    os.path.join(OUTPUT_DIR, "combined_data.csv.zip"),
    index = False,
    compression = "zip"
)
