#!/usr/bin/env python3

import requests
from pprint import pprint

url = 'http://localhost:2224/searched'

all_resp = requests.get(f"{url}/All").json()
char_resp = requests.get(f"{url}/Character").json()
fruit_resp = requests.get(f"{url}/Devil Fruit").json()
class_resp = requests.get(f"{url}/Class").json()
sub_resp = requests.get(f"{url}/Subclass").json()
stat_resp = requests.get(f"{url}/Status").json()
awakened_resp = requests.get(f"{url}/Awakened").json()

pprint(char_resp)