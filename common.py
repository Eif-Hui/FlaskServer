# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 下午11:54
# @Author  : Hui
# @File    : common.py

import requests
class Common(object):

    def __init__(self,host):
        self.uri = host

    def get(self,path,params=None,header=None):
        url = self.uri + path + params
        res = requests.get(url= url,headers= header,verify=False)
        return res

    def post(self,path,params,header=None):
        url = self.uri + path
        res = requests.post(url= url,json= params,headers= header,verify= False)
        return res

