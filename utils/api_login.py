import requests
from utils.config import BASE_URL, HEADERS

def login(payload):
     url = f"{BASE_URL}/login"
     response = requests.post(url, json=payload, headers=HEADERS)
     return response