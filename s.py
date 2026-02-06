import requests

url = "http://127.0.0.1:8000/api/book/"
data = {
    "title": "Война и мир",
    "author": "Лев Толстой",
    "price": 1500.00,
    "description": "Роман-эпопея"
}

response = requests.post(url, json=data)
print(response.status_code)  # 201 - Created
print(response.json())