import requests
# for single instance
# URL = "http://127.0.0.1:8000/stuinfo/1"

# for queryset 
URL = "http://127.0.0.1:8000/stuinfo/"

r = requests.get(url = URL)
data = r.json()
print(data)
