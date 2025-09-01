#使用数据库原生结合fixture进行参数化

import pytest
import requests
import json

#from utils.mysql_utils import get_mysql_case_data #第一种导入方法
# import utils.mysql_utils as um
import utils.excel_utils as ue
from config.const import URL 

url = URL

# # 借助一个工具方法获取数据库中的数据
# @pytest.fixture(params=um.get_mysql_case_data("登录"))
# def get_mysql_login_data(request):
#     return request.param

# @pytest.mark.skip
# def test_mysql_login1(get_mysql_login_data):
#     # print(get_mysql_login_data)
#     id = get_mysql_login_data[0]
#     case_id = get_mysql_login_data[1]
#     title = get_mysql_login_data[2]
#     interface_type = get_mysql_login_data[3]
#     uri = get_mysql_login_data[4]
#     method = get_mysql_login_data[5]
#     if_login = get_mysql_login_data[6]
#     input_data = get_mysql_login_data[7]
#     data_type = get_mysql_login_data[8]
#     expect = get_mysql_login_data[9]
#     if method == "get":
#         response = requests.get(url+uri, json.loads(input_data))
#         assert response.status_code == 200
#         # print(json.loads(response.text))
#         assert int(expect) == json.loads(response.text)["status"]
#     elif method == "post":
#         if data_type == "form":
#             response = requests.post(url+uri, data=json.loads(input_data))
#         elif data_type == "json":
#             response = requests.post(url+uri, json=json.loads(input_data))
#         assert 200 == response.status_code
#         assert int(expect) == json.loads(response.text)["status"]


# @pytest.fixture(params=um.get_mysql_case_data_for_pandas("登录"))
# def get_mysql_login_data_for_pandas(request):
#     return request.param


# def test_mysql_login2(get_mysql_login_data_for_pandas):
#     # print(get_mysql_login_data_for_pandas)
#     pandas_dict = get_mysql_login_data_for_pandas
#     if pandas_dict['method'] == "get":
#         response = requests.get(url+pandas_dict['uri'],
#                                 json.loads(pandas_dict['input_data']))
#         assert response.status_code == 200
#         assert int(pandas_dict['expect']) == json.loads(response.text)["status"]
#     elif pandas_dict['method'] == "post":
#         if pandas_dict['data_type'] == "form":
#             response = requests.post(url+pandas_dict['uri'],
#                                      data=json.loads(pandas_dict['input_data']))
#         elif pandas_dict['data_type'] == "json":
#             response = requests.post(url+pandas_dict['uri'],
#                                      json=json.loads(pandas_dict['input_data']))
#         assert response.status_code == 200
#         assert int(pandas_dict['expect']) == json.loads(response.text)["status"]


@pytest.mark.parametrize([
    'case_id',
    'title',
    'interface_type',
    'uri',
    'method',
    'if_login',
    'input_data',
    'data_type',
    'expect'], ue.fetch_excel_data("登录"))

def test_excel_login(case_id,
                     title,
                     interface_type,
                     uri,
                     method,
                     if_login,
                     input_data,
                     data_type,
                     expect):
    if method == "get":
        response = requests.get(url+uri, json.loads(input_data))
        assert response.status_code == 200
        # print(json.loads(response.text))
        assert int(expect) == json.loads(response.text)["status"]
    elif method == "post":
        if data_type == "form":
            response = requests.post(url+uri, data=json.loads(input_data))
        elif data_type == "json":
            response = requests.post(url+uri, json=json.loads(input_data))
        assert 200 == response.status_code
        assert int(expect) == json.loads(response.text)["status"]