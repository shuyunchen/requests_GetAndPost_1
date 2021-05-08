#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/9 1:58
# @Author  : 陈庆云
# @File    : get_token.py
# @Software: PyCharm
import requests
import yaml


def get_toke():
    params = {
        "corpid": "wwf7515791a226cb78",
        "corpsecret": "eftuO73EXi9h_hvML7wMO8Yk-6ZQ0HfgLcNZKR7o-lw",
    }
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    r = requests.get(url, params=params)
    token = r.json()['access_token']
    print(token)
    with open('token.yaml', 'w') as f:
        yaml.safe_dump(token, f)


if __name__ == '__main__':
    get_toke()
