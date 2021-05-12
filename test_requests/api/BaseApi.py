#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 0:29
# @Author  : 陈庆云
# @File    : BaseApi.py
# @Software: PyCharm
import requests


class BaseApi:
    def __init__(self):
        # 获取token
        params = {
            "corpid": "wwf7515791a226cb78",
            "corpsecret": "eftuO73EXi9h_hvML7wMO8Yk-6ZQ0HfgLcNZKR7o-lw",
        }
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        r = requests.request('get', url, params=params)
        self.token = r.json().get('access_token')
        self.s = requests.session()
        self.s.params = {"access_token": self.token}

    def send(self, *args, **kwargs):
        r = self.s.request(*args, **kwargs)
        print('******************')
        print(r.request.url)
        return r.json()
