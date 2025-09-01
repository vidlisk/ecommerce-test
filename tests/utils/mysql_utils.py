# 本文件中都是能很方便操作数据库的方法
import pymysql
import pandas as pd
from flask import json

def get_sql_connection():
    db_info = {
        "host": "192.168.0.193",
        "user": "root",
        "password":"root",
        "database": "mydb2",
        "charset": "utf8"
    }
    conn = pymysql.connect(**db_info)
    return conn

# def get_mysql_case_data():
def get_mysql_case_data(interface_type):
    conn = get_sql_connection()
    sql = "select * from mumu where interface_type = '{}'".format(interface_type)
    # sql = "select * from mumu"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

#与pymysql相比，pandas要对数据格式进行转换和解析
def get_mysql_case_data_for_pandas(interface_type):
    conn = get_sql_connection()
    sql = "select * from mumu where interface_type = '{}'".format(interface_type)
    interface_type_data = pd.read_sql(sql, conn)
    #解析数据
    final_data = []
    for i in interface_type_data.index:
        inner_data = {}
        for d in interface_type_data.iloc[[i]]:
            inner_data[d] = interface_type_data[d][i]
        final_data.append(inner_data)
    return final_data

# test_list = [] 
# interface_type_data = "登录"
# test_list = get_mysql_case_data_for_pandas(interface_type_data)
# print(test_list)