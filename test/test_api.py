import os

import requests


TOKEN = os.environ.get("API_TOKEN")

response = requests.get(
  "http://localhost:8080/api/v1/bot/status",
  headers={
    "Content-Type": "application/json", 
    "Authorization": f"Bearer {TOKEN}"
  }
)
print(response.status_code)
print(response.json())