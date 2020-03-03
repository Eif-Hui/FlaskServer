# -*- coding: utf-8 -*-
# @Time    : 2020/2/6 上午9:17
# @Author  : Hui
# @File    : test_.py


import pytest,allure,requests
from pyTest.pyTestCom import Common
com = Common('http://127.0.0.1:5000')

data = [("/api/v1.0/tasks",{"dd":"中国"},"demo1a",{"tasks": {"dd": "中国"}},{"tasks": {"dd": "中国"}}),
        ("/api/v1.0/tasks",{"dd":"中国"},"demo2a",{"tasks": {"dd": "中国"}},{"tasks": {"dd": "中国"}}),
        ("/api/v1.0/tasks",{"dd":"中国"},"demo3a",{"tasks": {"dd": "中国"}},{"tasks": {"dd": "中国"}})
]

@allure.feature('test 文件夹名模块名')
@pytest.mark.parametrize('path,par,title,expect,expectResult', data)
class TestHotWheelsRunOrderList(object):

    @allure.story('test 文件名')
    def test_PageListByStateList(self,path,par,title,expect,expectResult):
        req = com.post(path,par)
        allure.attach(req.request.body)    #  用例参数，类似log
        allure.dynamic.title(title)  # 参数化用例标题title
        assert expect == expectResult

if __name__ == '__main__':
    pytest.main()