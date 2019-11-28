# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : 6计算圆面积.py
# @time    : 2019-11-2810:01
# @Author  : zhangshan33

"""
圆面积
S=πr²
"""
π = 3.14
r = float(input('第一个数'))
s = π * r * r
print(s)


# 函数
def r1(r):
    π = 3.14
    return π * r * r


print(r1(2))

"""
实例
"""


def findArea(r):
    PI = 3.142
    return PI * (r * r)


# 调用方法
print("圆的面积为 %.6f" % findArea(5))
