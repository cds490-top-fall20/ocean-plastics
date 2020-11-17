import json
import os
import random
import time

import pandas as pd
import requests

PROJECT_DIR = os.path.dirname(
            os.path.dirname(
                os.path.dirname(__file__)))

DATA_DIR = os.path.join(PROJECT_DIR, "data", "raw", "mdt")

page_size = 10000
current_page = 1
all_data = []

while True:
    print("On page", current_page)
    page_url = f"https://marinedebris.engr.uga.edu/mdtapp/sendAllItemInstances.php?page={current_page}&page_size={page_size}&from=2015-01-01&to=2020-09-30"
    p = requests.get(page_url)
    if p.ok == False:
        raise Exception("Could not request page "+str(current_page))
    pj = p.json()
    total_records = pj["total_records"]
    if pj["success"] != True:
        raise Exception("API error on page "+str(current_page)+": "+pj["reason"])
    with open(f"{DATA_DIR}/mdt-p{current_page}.txt", "w") as f:
        json.dump(pj["data"], f)
    if current_page == int(total_records / page_size) + 1:
        break
    current_page += 1
    time.sleep(30 + 60 * random.random())


all_files_dfs = []
for page_file in sorted(os.listdir(DATA_DIR)):
    print(page_file)
    all_files_dfs.append(
        pd.read_json(
            os.path.join(DATA_DIR, page_file),
            convert_dates=False
            )
        )
full_df = pd.concat(all_files_dfs)

full_df.rename(
    columns = {
        "timestamp": "orig_timestamp"
    },
    inplace = True
)
full_df["timestamp"] = pd.to_datetime(full_df["orig_timestamp"], format='%Y%m%d%H%M%S')

full_df.sort_values(by="timestamp").to_csv(f"{DATA_DIR}/all_mdt.csv", index = False)
