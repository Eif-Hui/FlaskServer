# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 上午9:56
# @Author  : Hui
# @File    : test_excelCase.py


import json
import unittest
import requests

from ddt import ddt,data,os
from unitTest.common.sendRequests import SendRequests
from unitTest.common.readExecl import ReadExcel
t=ReadExcel()
excel_path = os.path.abspath("../dataList/excelCase.xlsx")
testData=t.readExcel(excel_path, "Sheet1")
#s = requests.session()#跨请求保持参数如cookie值

@ddt
class Test1(unittest.TestCase):
    def setUp(self):
        pass

   #运行后用例会根据驱动加载的数据自动加载成多个单独的用例执行
    @data(*testData)
    def test_(self,data):
        re = SendRequests().sendRequests(requests,data)#调用公共模块执行用例
        print("响应参数为：{response}\nResponse code：{code} ".format(response=re.text, code=re.status_code).encode("UTF-8"))
        self.assertEqual(re.status_code,200)
        check = data["checkpoint"]
        print("检查点-->：{check} ".format(check = check))
        self.assertIn(check, re.text)


if __name__ == '__main__':
    unittest.main()