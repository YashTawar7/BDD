import requests
import pytest


@pytest.fixture
def login():
    login_url = "http://10.100.15.32:9081/com.ibm.mdm.server.ws.restful/login"
    login_data = {
        "username": "your_username",
        "password": "your_password"
    }
    response = requests.post(login_url, json=login_data)
    assert response.status_code == 200
    token = response.json().get('token')
    yield token
    # Add logout logic if necessary


def test_mdm_server_reachable(login):
    url = "http://10.100.15.32:9081/com.ibm.mdm.server.ws.restful/resources/MDM/matchcode/resolveMatchCode"
    headers = {"Authorization": f"Bearer {login}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    print(response.json())  # Print the response JSON
