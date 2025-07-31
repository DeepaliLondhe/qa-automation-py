import json
import pytest
from utils.api_helpers import create_user

@pytest.mark.smoke
def test_create_user():
    # Load test data from JSON file
    with open("testdata/users_payload.json", "r") as file:
        payload = json.load(file)

    # Call helper to hit API
    response = create_user(payload)

    # Assertions
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["name"] == payload["name"]
    assert response_data["job"] == payload["job"]
