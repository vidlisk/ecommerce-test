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

# 在 pytest 收集测试用例时，将 Unicode 编码转换为可读中文。
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
