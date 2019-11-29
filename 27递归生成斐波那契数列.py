# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : 27递归生成斐波那契数列.py
# @time    : 2019-11-2821:57
# @Author  : zhangshan33

def r(n):
    if n <= 1:
        return n
    else:
        return (r(n - 1) + r(n - 2))


num = int(input('数字'))

for i in range(num):
    print(r(i))

