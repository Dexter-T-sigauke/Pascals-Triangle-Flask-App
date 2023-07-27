import requests

url = 'http://localhost:8080/pascals-triangle'
data = {
    "rows": 5
    }

response = requests.post(url, json=data)
print(response.json())
