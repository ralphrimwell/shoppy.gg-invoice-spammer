from json import JSONDecodeError
from urllib import request
import requests
# import aiohttp
import random
import string
import time

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


product = input("input product code eg: [(https://shoppy.gg/product/0sv149x) (0sv149x is your product code)] ")
while True:
    data = {
        "email": f"{get_random_string(10)}@gmail.com",
        "fields": [],
        "gateway": "BTC",
        "product": "0sv149x",
        "quantity": 1
    }
    data = requests.put('https://shoppy.gg/api/v1/public/order/store', json=data)
    try:
        json = data.json()
    except requests.exceptions.JSONDecodeError:
        print('sleep')
        time.sleep(5)
    print(json)
