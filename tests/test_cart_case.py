import pytest
import requests
import json

# import utils.mysql_utils as um
import utils.excel_utils as ue

from config.const import URL 

@pytest.fixture()
def get_token(get_login_token):
    return get_login_token

@pytest.fixture()
def get_params():
    return ue.fetch_excel_data("购物车")

# @pytest.mark.skip
def test_excel_cart_add(get_token,get_params):
    params = get_params
    # print(params)
    jwt_token = get_token
    for request_data in params:
        print(request_data)
        print("#" * 20)
        case_id = request_data['编号']
        title = request_data['标题']
        interface_type = request_data['请求接口类别']
        uri = request_data['请求地址']
        method = request_data['请求方式']
        if_login = request_data['是否需要登录']
        input_data = request_data['输入数据']
        data_type = request_data['数据格式']
        expect = request_data['期望结果']
        print(f"用例编号：{case_id}")
        print("*" * 20)
        if if_login == 1:
            headers = {
                "jwt_token":jwt_token
            }
            if method == "get":
                response = requests.get(URL+uri,
                                        input_data,
                                        headers=headers)
                assert 200 == response.status_code
                assert expect == json.loads(response.text)['status']
            elif method == "post":
                if data_type == "form":
                    response = requests.post(URL+uri,data=input_data,headers=headers)
                    assert 200 == response.status_code
                    assert expect == json.loads(response.text)['status']
                elif data_type == "json":
                    response = requests.post(URL + uri, json=input_data, headers=headers)
                    assert 200 == response.status_code
                    assert expect == json.loads(response.text)['status']
        elif if_login == 0:
            if method == "get":
                response = requests.get(URL+uri,
                                        input_data,
                                        headers=headers)
                assert 200 == response.status_code
                assert expect == json.loads(response.text)['status']
            elif method == "post":
                if data_type == "form":
                    response = requests.post(URL+uri,data=input_data)
                    assert 200 == response.status_code
                    assert expect == json.loads(response.text)['status']
                elif data_type == "json":
                    response = requests.post(URL + uri, json=input_data)
                    assert 200 == response.status_code
                    assert expect == json.loads(response.text)['status']