#!/usr/bin/env python3

import requests
from pprint import pprint

url = 'http://localhost:2224/searched'

# vast number of endpoints depending on combined search criteria
# below only returns results for All and singular criteria search
all_resp = requests.get(f"{url}/All").json()
char_resp = requests.get(f"{url}/Character").json()
fruit_resp = requests.get(f"{url}/Devil Fruit").json()
class_resp = requests.get(f"{url}/Class").json()
sub_resp = requests.get(f"{url}/Subclass").json()
stat_resp = requests.get(f"{url}/Status").json()
awakened_resp = requests.get(f"{url}/Awakened").json()

# print(char_resp)

for x in all_resp:
    print(f'{x["Character"]} {x["Status"]} the {x["Devil Fruit"]} devil fruit. It is a {x["Class"]} type fruit, subclass {x["Subclass"]}.\n')