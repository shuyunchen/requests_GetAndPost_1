#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 0:02
# @Author  : 陈庆云
# @File    : address.py
# @Software: PyCharm
from test_requests.api.BaseApi import BaseApi


class Address(BaseApi):
    def __init__(self):
        super().__init__()

    def add_member(self, userid: str, name: str, mobile: str, department: list, **kwargs):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        userinfo = {
            "userid": userid,
            "name": name,
            "alias": name,
            "mobile": mobile,
            "department": department
        }
        r = self.send('post', url, json=userinfo)
        return r

    def detect_member(self, userid):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}'
        r = self.send('get', url)
        return r

    def update_member(self, userid: str, name: str):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        userinfo = {
            "userid": userid,
            "name": name,
        }
        r = self.send('post', url, json=userinfo)
        return r

    def delete_member(self, userid):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}'
        r = self.send('get', url)
        return r
