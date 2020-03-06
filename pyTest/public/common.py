# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 下午11:54
# @Author  : Hui
# @File    : pyTestCom.py

import requests
class Common(object):

    def __init__(self,host):
        self.uri = host

    def get(self,path,params=None,header=None):
        url = self.uri + path
        res = requests.get(url= url,params= params,headers= header,verify=False)
        return res

    def post(self,path,params,header=None):
        url = self.uri + path
        res = requests.post(url= url,json= params,headers= header,verify= False)
        return res

