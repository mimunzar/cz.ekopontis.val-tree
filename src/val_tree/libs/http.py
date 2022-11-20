#!/usr/bin/env python3
import requests


JSON_HEADER = {'Content-Type': 'application/json'}
def post(url, data):
    r = requests.post(url, headers = JSON_HEADER, json = data)
    r.raise_for_status()
    return r.json()

