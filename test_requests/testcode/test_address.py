#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 0:02
# @Author  : 陈庆云
# @File    : test_address.py
# @Software: PyCharm
import pytest
import yaml

from test_requests.api.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()

    @pytest.mark.parametrize('userid, name, mobile', yaml.safe_load(open('test_data.yaml')))
    def test_address(self, userid, name, mobile):
        self.address.delete_member(userid=userid)
        self.address.add_member(userid=userid, name=name, mobile=mobile, department=[1, 2])
        r = self.address.detect_member(userid=userid)
        assert r.get('name', '不存在') == name
