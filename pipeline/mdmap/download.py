import json
import random
import time

import requests

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
    with open(f"data/raw/mdmap/mdmap-p{current_page}.txt", "w") as f:
        json.dump(pj["data"], f)
    if current_page == int(total_records / page_size) + 1:
        break
    current_page += 1
    time.sleep(30 + 60 * random.random())



