# -*- coding: utf-8 -*-
# @Time    : 2020/2/6 上午9:17
# @Author  : Hui
# @File    : test_.py


import pytest,allure
payload = [(1,2,"待支付"),
         (3,4,"待分配"),
         (5,6,"待取货"),
         (7,8,"配送中"),
         (9,10,"全部任务查询")]

@allure.feature('pytest 参数化demo')
@pytest.mark.parametrize('data,aer,describe', payload)
class TestHotWheelsRunOrderList(object):

    @allure.story('')
    def test_PageListByStateList(self,data,aer,describe):
        """丰伙轮管理台跑腿任务-->{}""".format(describe)
        #allure.attach(describe)
        assert data+1 == aer

if __name__ == '__main__':
    pytest.main()