#!/usr/bin/env python3

import requests
from pprint import pprint

url = 'http://localhost:2224/character'
resp = requests.get(url).json()

pprint(resp)