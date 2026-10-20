import requests
import json
import time
import os
from datetime import datetime

while True:
    position = requests.get("http://api.open-notify.org/iss-now.json").json()
    os.system("cls")
    print(f"{position["timestamp"]} [{datetime.now().strftime("%H:%M:%S")}]: ")
    value = list(position["iss_position"].values())
    key = list(position["iss_position"].keys())
    for i in range(len(position["iss_position"])):
        print(f"{key[i].title()}: {value[i]}")
    time.sleep(10)
