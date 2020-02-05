# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 上午11:58
# @Author  : Hui
# @File    : connect_db.py

import pymysql,os
from debugEif import BodyVerify
curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "config.ini")
def get_sql_conn():
    """
    获取数据库连接
    """
    conn = pymysql.connect(host='***.***.***.**',
                           port='***',
                           user='***',
                           password='***',
                           db='***')

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
    con, cursor = get_sql_conn()
    return get_dict_data_sql(cursor, sql)[0]

if __name__ == '__main__':
    sql = "SELECT * from h_logistics_order WHERE order_no = 'PT202001201452776977'"
    dd = main(sql)
    print(dd)