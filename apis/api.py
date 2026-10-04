import requests

url = "http://api.open-notify.org/astros.json"

response = requests.get(url, timeout=10)
data = response.json()
print(data)


print(response.status_code)
print(response.json())