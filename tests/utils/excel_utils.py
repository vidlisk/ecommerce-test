import pandas
import os

def fetch_excel_data(interface_type):
    # data = pandas.read_excel(".\case_data\test_cases.xlsx")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    excel_path = os.path.join(base_dir, "..", "case_data", "test_cases.xlsx")
    data = pandas.read_excel(excel_path)
    interface_type_data = data[data['请求接口类别'] == interface_type]
    final_data = []
    start_index = 0
    for i in interface_type_data.index:
        inner_data = {}
        # for d in interface_type_data.iloc[[i]]: #原先的报错写法
        for d in interface_type_data.iloc[[start_index]]:
            inner_data[d] = interface_type_data[d][i]
        final_data.append(inner_data)
        start_index += 1
    return final_data

# test_list = []
# interface_type_data = "购物车"
# test_list = fetch_excel_data(interface_type_data)
# print(test_list)