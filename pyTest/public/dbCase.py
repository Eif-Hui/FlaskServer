# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 下午3:36
# @Author  : Hui
# @File    : dbCase.py
import pymysql
def read_db():
    """
    :return: 链接数据库，获取数据库全部测试用例，以为list形式返回
    """
    db = pymysql.connect(host='120.77.202.176',
                           port=3306,
                           user='root',
                           password='Password.01',
                           db='testcase',
                           charset='utf8')

    # 执行sql语句
    cursor = db.cursor()  # 使用cursor()方法获取操作游标
    sql = "SELECT * from TestCaseList"
    cursor.execute(sql)
    info = cursor.fetchall()
    db.commit()
    cursor.close()  # 关闭游标
    db.close()  # 关闭数据库连接

    return list(info)
print(read_db())