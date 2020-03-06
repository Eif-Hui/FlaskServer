# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 下午11:00
# @Author  : Hui
# @File    : database.py
import pymysql
def init_database(): #连接数据库
    try:
        conn = pymysql.connect(host='120.77.202.176',
                           port=3306,
                           user='root',
                           password='Password.01',
                           db='testcase',
                           charset='utf8')
        cursor = conn.cursor()
        return conn,cursor
    except:
        print('Error:数据库连接失败')
        return None

def insert_database(sql,*args):#插入数据
    conn, cursor = init_database()
    cursor.execute('use testcase')
    try:
        cursor.execute(sql,args)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except:
        print("Error:数据插入失败")
        return None

def select_data(sql, *args):#查询数据
    try:
        conn, cursor = init_database()
        cursor.execute('use testcase')
        cursor.execute(sql, args)
        datas =  cursor.fetchall()
        cursor.close()
        conn.close()
        return datas
    except:
        print("Error:数据查找错误")
        return None

def update_report(sql): #更新report统计表
    try:
        conn, cursor = init_database()
        cursor.execute('use data_collection_platform')
        cursor.execute('truncate table report')
        cursor.execute(sql)
        cursor.execute('update report set Rate =  Seccess/(Seccess+Fail)*100') #成功或者失败数有可能为NULL，需要重新计算
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except:
        print("Error:更新统计表失败")
        return None