# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : 5计算三角形的面积.py
# @time    : 2019-11-2809:55
# @Author  : zhangshan33

"""
输入三个数
求三角形面积 长*高*宽

"""
a = float(input('第一个数'))
b = float(input('第二个数'))
c = float(input('第三个数'))

# 周长
s = (a+b+c)/2

# 面积
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(area)

"""
实例
"""
a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))

# 计算半周长
s = (a + b + c) / 2

# 计算面积
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('三角形面积为 %0.2f' % area)