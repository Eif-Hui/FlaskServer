# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 上午11:58
# @Author  : Hui
# @File    : sqlExpect.py

import pymysql

def getSql():
    """
    获取数据库连接
    """
    conn = pymysql.connect(host='120.77.202.176',
                           port=3306,
                           user='root',
                           password='Password.01',
                           db='testcase',
                           charset='utf8')

    cursor = conn.cursor()
    return conn, cursor


def get_index_dict(cursor):
    """
    获取数据库对应表中的字段名
    """
    index_dict = dict()
    index = 0
    for desc in cursor.description:
        index_dict[desc[0]] = index
        index = index + 1
    return index_dict


def get_dict_data_sql(cursor, sql):
    """
    运行sql语句，获取结果，并根据表中字段名，转化成dict格式（默认是tuple格式）
    """
    cursor.execute(sql)
    data = cursor.fetchall()
    index_dict = get_index_dict(cursor)
    res = []
    for datai in data:
        resi = dict()
        for indexi in index_dict:
            resi[indexi] = datai[index_dict[indexi]]
        res.append(resi)
    return res

def main(sql):
    con, cursor = getSql()
    return get_dict_data_sql(cursor, sql)[0]

if __name__ == '__main__':
    sql = "SELECT * from TestCaseList"
    dictSql = main(sql)
    print(dictSql)


