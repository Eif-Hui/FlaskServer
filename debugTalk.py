# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 下午7:24
# @Author  : Hui
# @File    : debugTalk.py

import datetime,random,string

class BodyVerify(object):

    def new_number(self):
        """
        :return: 根据当前时间生成唯一数
        """
        NewData = '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())
        soleDate = NewData[3:]
        return soleDate

    def gen_random_str(self,str_len):
        return ''.join(random.choice(string.digits) for _ in range(str_len)) #string.ascii_letters + 英文字符



if __name__ == '__main__':
    req = BodyVerify()
    req.gen_random_str(12)