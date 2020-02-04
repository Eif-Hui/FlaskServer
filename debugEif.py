# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 下午7:24
# @Author  : Hui
# @File    : debugEif.py

import datetime,random,string,yaml,os

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
        :param file:  YAML文件路径
        :return: 读取YAML文件，最终转化为json 输出
        """
        file = open(file, 'r', encoding ='utf-8')
        file_data = yaml.load(file.read())
        return file_data



if __name__ == '__main__':
    current_path =  os.path.abspath(".")  # 当前路径
    yamlPath = os.path.join(current_path,'data/yamldemo.yaml')

    req = BodyVerify()
    req.read_yaml(yamlPath)