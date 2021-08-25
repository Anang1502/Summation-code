from flask import Flask, request
import requests
import json

json = json.loads(json.dumps({"n1": 1, "n2": 2}))

r = requests.post('http://127.0.0.1:5009/add', json=json)

print(r.json())