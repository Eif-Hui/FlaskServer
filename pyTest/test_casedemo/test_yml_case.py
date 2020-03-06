# -*- coding: utf-8 -*-
# @Time    : 2020/2/6 上午9:17
# @Author  : Hui
# @File    : test_yml_case.py


import pytest,allure,os
from pyTest.public.pyTestCom import Common
from pyTest.public.pyTestCom import readYaml
com = Common('http://127.0.0.1:5000')

data = [("/api/v1.0/tasks",{"dd":"中国"},"demo1a",{"tasks": {"dd": "中国"}},{"tasks": {"dd": "中国"}}),
        ("/api/v1.0/tasks",{"dd":"中国"},"demo2a",{"tasks": {"dd": "中国"}},{"tasks": {"dd": "中国"}}),
        ("/api/v1.0/tasks",{"dd":"中国"},"demo3a",{"tasks": {"dd": "中国"}},{"tasks": {"dd": "中国"}})
]


curPath = os.path.dirname(os.path.realpath(__file__))
filePath = os.path.join(curPath, '../caseData/ymlDemo.yaml')
params = readYaml(filePath) # 用例和数据分离，数据以yaml方式存储

@allure.feature('test 一级标题')
@pytest.mark.parametrize('path,reqPar,title,expect,expectResult', params)
class TestRunOrderList(object):

    #@allure.story('test 二级标题')
    def test_PageListByStateList(self,path,reqPar,title,expect,expectResult):
        req = com.post(path,reqPar)
        allure.attach(req.request.body)    #  用例参数，类似log
        allure.dynamic.story('test 二级标题')   # 二级标签
        allure.dynamic.title(title) # 用例ID+接口名称
        # desc = "<font color='red'>请求路径:</font>{}<Br/>"" \
        # ""<font color='red'>请求类型:<>/font{}<Br/>"" \
        # ""<font color='red'>期望结果:</font>{}<Br/>"" \
        # ""<font color='red'>实际结果描述:</font>{}<Br/>".format(path,"post",expect,expectResult)
        # allure.dynamic.description(desc)
        assert expect == expectResult

if __name__ == '__main__':
    pytest.main()