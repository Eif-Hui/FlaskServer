# -*- coding: utf-8 -*-
# coding:utf-8
# @Time    : 2020/3/2 下午11:54
# @Author  : Hui
# @File    : pyTestCom.py

def readYaml(file):
    """
    :param file:  YAML文件路径
    :return: eval函数的作用是将传入的字符串作为表达式来进行计算
    可以有效去除(双)引号，空格等字符。
    """
    file = open(file, 'r', encoding='utf-8')
    file_data = file.read()
    return eval(file_data)

import requests,json
class Common(object):

    def __init__(self,host):
        self.uri = host

    def get(self,path,params=None,header=None):
        url = self.uri + path
        res = requests.get(url= url,params= eval(params),headers= header,verify=False)
        return res
    def post(self,path,params,header=None):
        url = self.uri + path
        res = requests.post(url= url,json= json.loads(params),headers= header,verify= False)
        return res

