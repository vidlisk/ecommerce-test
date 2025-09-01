from config.const import URL
import requests
import pytest
import json

@pytest.fixture(scope="session", autouse=True)
def get_login_token():
    login_uri = "/loginWithJwt"
    login_data = {
        "userName": "imooc",
        "password": "12345678"
    }
    login_response = requests.get(URL+login_uri, login_data)
    data = json.loads(login_response.text)
    jwt_token = data["data"]
    return jwt_token