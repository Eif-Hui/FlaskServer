# -*- coding: utf-8 -*-
# @Time    : 2020/2/6 上午9:17
# @Author  : Hui
# @File    : test_yml_case.py


import pytest,allure
from pyTest.pyTestCom import Common
from pyTest.db_connect import read_db
from pyTest.connect_db import *
com = Common('http://127.0.0.1:5000')
@allure.feature('test 一级标签')
@pytest.mark.parametrize('caseId,story,title,method,path,req_data,sql,expect1,expect2,expect3', read_db())
class TestDbCase(object):

    def test_db_case(self,caseId,story,title,method,path,req_data,sql,
                                 expect1,expect2,expect3):
        if method == "post" or method == "Post" or method == "POST":
            req = com.post(path,req_data)
        elif method == "get" or method == "Get" or method == "GET":
            req = com.get(path,req_data)
        allure.attach(req.request.body)
        allure.dynamic.story(story)   # 二级标签
        allure.dynamic.title(caseId+title)
            # desc = "<font color='red'>请求路径:</font>{}<Br/>"" \
            # ""<font color='red'>请求类型:<>/font{}<Br/>"" \
            # ""<font color='red'>期望结果:</font>{}<Br/>"" \
            # ""<font color='red'>实际结果描述:</font>{}<Br/>".format(path,"post",expect,expectResult)
            # allure.dynamic.description(desc)
        assert 'success' == main(sql)['expect2']
        assert expect1 != expect2
        assert sql != expect3

if __name__ == '__main__':
    pytest.main()