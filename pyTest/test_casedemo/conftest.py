# -*- coding: utf-8 -*-
# @Time    : 2020/2/7 上午9:02
# @Author  : Hui
# @File    : conftest.py

import pytest

@pytest.fixture()
def Assert():
    headers = "a"
    return headers