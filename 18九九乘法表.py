# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : 18九九乘法表.py
# @time    : 2019-11-2813:08
# @Author  : zhangshan33
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}*{i}={j * i}', end=' ')
