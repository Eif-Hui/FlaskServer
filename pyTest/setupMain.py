# -*- coding: utf-8 -*-
# @Time    : 2020/2/6 上午9:19
# @Author  : Hui
# @File    : setupMain.py

import os
import subprocess
import pytest

def invoke(md):
    """
    :param md:
    :return:
    """
    output, errors = subprocess.Popen(md, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    o = output.decode("utf-8")
    return output


if __name__ == '__main__':
    PATH = os.getcwd()
    xml_report_path = PATH + "/report/xml"
    html_report_path = PATH + "/report/html"
    #pytest.main(['--reruns 2'])

    args = ['-s', '-q', '--alluredir', xml_report_path]
    pytest.main(args)
    cmd = 'allure generate {xml} -o {html}'.format(xml=xml_report_path,html=html_report_path)
    p = os.popen(cmd).read().strip()  # 运作终端命令
    #pytest.main(cmd)
    #invoke(cmd)