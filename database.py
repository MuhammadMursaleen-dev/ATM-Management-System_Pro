import os
import json

DATAFILE = "database.json"

def load_data():
    if not os.path.exists(DATAFILE):
        return []
    with open (DATAFILE,"r",encoding = "utf-8" ) as file:
        data = json.load(file)
        return data
def save_data(customers):
    with open (DATAFILE,"w",encoding="utf-8") as file:
        json.dump(customers,file,indent= 4)
