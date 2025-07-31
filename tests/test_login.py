import pytest
import json
from utils.api_login import login

def test_user_login():
      # Load test data from JSON file
    with open("testdata/login.json", "r") as file:
        payload = json.load(file)

    # Call helper to hit API
    response = login(payload)

    # Assertions
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == payload["name"]
    assert response_data["job"] == payload["job"]