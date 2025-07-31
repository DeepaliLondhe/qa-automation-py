import requests
from utils.config import BASE_URL, HEADERS

def create_user(payload):  # 👈 THIS LINE MUST HAVE 'payload'
    url = f"{BASE_URL}/users"
    response = requests.post(url, json=payload, headers=HEADERS)
    return response
