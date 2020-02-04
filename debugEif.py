# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 下午7:24
# @Author  : Hui
# @File    : debugEif.py

import datetime,random,string,yaml

class BodyVerify(object):

    def new_number(self):
        """
        :return: 根据当前时间生成唯一数
        """
        NewData = '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())
        soleDate = NewData[3:]
        return soleDate

    def gen_random_str(self,str_len):
        """
        :param str_len:
        :return: 生存指定长度的随机字符串
        """
        return ''.join(
            random.choice(string.digits) for _ in range(str_len)) #string.ascii_letters + 英文字符

    def read_yaml(self,file):
        """
        :return: 读取yaml文件，转为json输出
        """
        with open(file,mode='r','utf-8') as file_config:
            dict_body = yaml.load(file_config.read())
            pass



if __name__ == '__main__':
    req = BodyVerify()
    req.gen_random_str(12)