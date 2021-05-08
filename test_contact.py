#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/9 2:02
# @Author  : 陈庆云
# @File    : test_contact.py
# @Software: PyCharm
import requests
import yaml


class TestContact:

    def test_add(self):
        token = yaml.safe_load(open('token.yaml'))
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}'
        userinfo = {
            "userid": "zhangsancqy",
            "name": "张三cqy",
            "alias": "jackzhang",
            "mobile": "+86 13800000102",
            "department": [1, 2]
        }
        r = requests.post(url, json=userinfo)
        print(r.json())
        assert r.json()['errcode'] == 0

    def test_search(self):
        token = yaml.safe_load(open('token.yaml'))
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=zhangsancqy'
        r = requests.get(url)
        print(r.json())
        assert r.json()['errcode'] == 0

    def test_update(self):
        token = yaml.safe_load(open('token.yaml'))
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}'
        userinfo = {
            "userid": "zhangsancqy",
            "name": "李四cqy",
        }
        r = requests.post(url, json=userinfo)
        print(r.json())
        assert r.json()['errcode'] == 0

    def test_delete(self):
        token = yaml.safe_load(open('token.yaml'))
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=zhangsancqy'
        r = requests.get(url)
        print(r.json())
        assert r.json()['errcode'] == 0
