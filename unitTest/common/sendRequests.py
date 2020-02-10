# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 上午10:00
# @Author  : Hui
# @File    : sendRequests.py

import os
from unitTest.common.readExecl import ReadExcel
import requests
import json
JQUrl = "http://10.202.201.79:8084"

class SendRequests():
    #s变量主要考虑登入之后的业务在留下的，apiData变量方便后续转参，这里更灵活
    def sendRequests(self,s,apiData):
        method = apiData["method"] #该接口的请求方式，对应表格中
        url = apiData["url"] #接口的url地址，对应表格中

        # 这个是属于get请求中的url中参数的提交方式
        if apiData["params"] == "":
            par = None
        else:
            # eval函数实现list、dict、tuple与str之间的转化
            par = eval(apiData["params"])

        test_nub = apiData['id']
        case_description = apiData['case_name']
        print("*******正在执行用例：--- {id} ---  {case_name}  ----**********".format(id= test_nub,case_name= case_description))
        print("请求方式：%s, 请求url:%s%s" % (method, JQUrl,url))
        print("请求headers：{header}".format(header=''))
        print("请求params：%s" % par)

        #接口中的体部信息
        if apiData["body"] == "":
            body_data = None
        else:
            body_data = eval(apiData["body"])

        #接口数据的提交方式：一个data和json
        type = apiData["type"]
        if type == "json":
            body = json.dumps(body_data)
        if type == "data":
            body = body_data
        else:
            body = body_data
        if method == "post":
            print("post请求body类型为：%s ,body内容为：%s" % (type, body))
        if method == "put":
            print("put 请求data类型为: {type},data内容为：{data}".format(type= type,data= body))

        #发送请求
        re = s.request(method=method,url=JQUrl + url,headers= "Token",params=par,json =body)
        return re

if __name__ == '__main__':
    excel_path = os.path.abspath("../dataList/excelCase.xlsx")
    t=ReadExcel()
    testData=t.readExcel(excel_path, "Sheet1")
    print(testData)
