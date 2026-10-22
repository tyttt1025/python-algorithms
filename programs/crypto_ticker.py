import requests
import json
import time
import os

while True:
    crypto = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether&vs_currencies=usd").json()
    os.system("cls")
    print(crypto)
    time.sleep(10)