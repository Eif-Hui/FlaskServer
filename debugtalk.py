# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 下午7:24
# @Author  : Hui
# @File    : debugtalk.py

import datetime
class BodyVerify(object):

    def new_number(self):
        """
        :return: 根据当前时间生成唯一数
        """
        NewData = '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())
        soleDate = NewData[3:]
        return soleDate



if __name__ == '__main__':
    req = BodyVerify()
    req.new_number()