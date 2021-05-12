#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 0:23
# @Author  : 陈庆云
# @File    : generate_yaml.py
# @Software: PyCharm
import yaml


def generate_yaml():
    data = [('test111', 'test111', '15845658741'),
            ('test112', 'test112', '15845658742'),
            ('test112', 'test112', '15845658743')]
    with open('test_data.yaml', 'w') as f:
        yaml.safe_dump(data, f)


generate_yaml()
