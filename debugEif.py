# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 下午7:24
# @Author  : Hui
# @File    : debugEif.py

import datetime, random, string, yaml, os,time
import configparser # 读取ini配置文件，实例化configparser对象

class BodyVerify(object):

    def newNumber(self):
        """
        :return: 根据当前时间生成唯一数
        """
        NewData = '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())
        soleDate = NewData[3:]
        return soleDate

    def randomStamp(self,a, b):
        """
        :param a:
        :param b:
        :return: 生成两数之间的整数
        """
        return random.randint(a, b)

    def randomTelephone(self):
        """
        :return: 生成随机手机号
        """
        preList = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153",
                   "155", "156", "157", "158", "159", "186", "187", "188", "199"]
        return random.choice(preList) + "".join(random.choice("0123456789") for i in range(8))

    def randomStr(self, str_len):
        """
        :param str_len:
        :return: 生存指定长度的随机字符串
        """
        return ''.join(
            random.choice(string.digits) for _ in range(str_len))  # string.ascii_letters + 英文字符

    def readYaml(self, file):
        """
        :param file:  YAML文件路径
        :return: 读取YAML文件，最终转化为json 输出
        """
        file = open(file, 'r', encoding='utf-8')
        file_data = yaml.load(file.read())
        return file_data

    def timeStamp(self,timeNum):
        """"
        :param # 输入毫秒级的戳，转出正常格式的时间 int
        :return str
        """
        timeStamp = float(timeNum / 1000)
        timeArray = time.localtime(timeStamp)
        return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

    def getConfig(self,filename, tp, key, value):
        """
        # 获取请求参数
        :param file: 配置文件,格式为ini格式
        :return: 返回key:value结构参数串
        """
        conf = configparser.ConfigParser()  # 实例化configparser对象
        conf.read(filename, encoding='utf-8')
        if tp == "int":
            return conf.getint(key, value)
        elif tp == "str":
            return conf.get(key, value)
        else:
            print('类型不存在')

# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# class SendEmail(object):
#     # 定义邮件并发送
#     global send_user
#     global email_host
#     global password
#     email_host = "smtp.163.com"
#     send_user = "13711153040@163.com"
#     password = "*******"
#
#     def send_mail(self, user_list, sub):
#         msgRoot = MIMEMultipart('related')
#         user = "Xie" + "<" + send_user + ">"
#         msgRoot['Subject'] = sub
#         msgRoot['From'] = user
#         msgRoot['To'] = ";".join(user_list)
#
#         # 发送正文
#         text = '麻烦下载附件查看测试详情，谢谢'
#         att1 = MIMEText(text, 'plain', 'utf-8')
#         msgRoot.attach(att1)
#
#         """
# 		测试报告存储路径,
# 		将测试报告文件夹下的所有文件名作为一个列表返回,
# 		对所有测试报告按照生成时间进行排序,
# 		获取最新的测试报告,
# 		指定最新的测试报告路径
# 		"""
#         report_dir = "../Report/"
#         lists = os.listdir(report_dir)  #
#         lists.sort(key=lambda filename: os.path.getmtime(report_dir + filename))
#         recent = lists[-1]
#         file = os.path.join(report_dir, recent)
#
#         # 发送附件
#         sendfile = open(file, "r", encoding='UTF-8').read()
#         att = MIMEText(sendfile, "base64", "utf-8")
#         att["Content-Type"] = "application/octet-stream"
#         att["Content-Disposition"] = "attachment;filename = 'API_TestReport.html'"
#         msgRoot.attach(att)
#         server = smtplib.SMTP()
#         server.connect(email_host)
#         server.login(send_user, password)
#         server.sendmail(user, user_list, msgRoot.as_string())
#         server.close()

import logging
nowTime = time.strftime('%Y%m%d', time.localtime(time.time()))
class TestLogger(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # os.getcwd()获取当前文件的路径，os.path.dirname()获取指定文件路径的上级路径
        log_path = os.path.join(os.path.dirname(os.getcwd()), '../data/log/')
        self.all_log_name = log_path + nowTime + '_' + '.log'
        # 创建一个handler写入所有日志
        all_fh = logging.FileHandler(self.all_log_name, mode='a', encoding='utf-8')
        all_fh.setLevel(logging.INFO)

        # 创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        all_formatter = logging.Formatter('[%(asctime)s] - %(filename)s - %(funcName)s - %(message)s')
        all_fh.setFormatter(all_formatter)

        # 给logger添加handler
        self.logger.addHandler(all_fh)
        self.logger.addHandler(ch)

        all_fh.close()
        ch.close()

    def get_log(self):
        return self.logger


if __name__ == '__main__':
    req = BodyVerify()
    curPath = os.path.dirname(os.path.realpath(__file__))
    cfgPath = os.path.join(curPath, "config.ini")   #  配置文件ini
    req.getConfig(cfgPath,'str','db','host')

    current_path = os.path.abspath(".")  # 当前路径
    yamlPath = os.path.join(current_path, 'data/yamldemo.yaml')
    req.readYaml(yamlPath)

