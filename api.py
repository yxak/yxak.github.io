import requests

r = requests.get("https://api.github.com/user/yxak")

while True:
    if r.status_code != 200:
        jsonned = str(r.json())
        print(jsonned.capitalize()
