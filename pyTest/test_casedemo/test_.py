# -*- coding: utf-8 -*-
# @Time    : 2020/2/6 上午9:17
# @Author  : Hui
# @File    : test_.py


import pytest,allure,os
from pyTest.pyTestCom import Common
from pyTest.pyTestCom import readYaml
com = Common('http://127.0.0.1:5000')

data = [("/api/v1.0/tasks",{"dd":"中国"},"demo1a",{"tasks": {"dd": "中国"}},{"tasks": {"dd": "中国"}}),
        ("/api/v1.0/tasks",{"dd":"中国"},"demo2a",{"tasks": {"dd": "中国"}},{"tasks": {"dd": "中国"}}),
        ("/api/v1.0/tasks",{"dd":"中国"},"demo3a",{"tasks": {"dd": "中国"}},{"tasks": {"dd": "中国"}})
]


curPath = os.path.dirname(os.path.realpath(__file__))
filePath = os.path.join(curPath, '../caseData/ymlDemo.yaml')
params = readYaml(filePath) # 用例和数据分离，数据以yaml方式存储

@allure.feature('test 一级标题')
@pytest.mark.parametrize('path,par,title,expect,expectResult', params)
class TestRunOrderList(object):

    @allure.story('test 二级标题')
    def test_PageListByStateList(self,path,par,title,expect,expectResult):
        req = com.post(path,par)
        allure.attach(req.request.body)    #  用例参数，类似log
        allure.dynamic.title(title)  # 三级标题，参数化用例标题title
        assert expect == expectResult

if __name__ == '__main__':
    pytest.main()