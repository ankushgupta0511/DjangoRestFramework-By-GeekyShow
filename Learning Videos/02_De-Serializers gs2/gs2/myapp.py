import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name':'11ankush1',
    'roll':102,
    'city':'1bhopal'
}



json_data = json.dumps(data)

r = requests.post(url = URL, data = json_data)

data = r.json()
print(data)