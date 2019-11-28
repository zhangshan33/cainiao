# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : 9交换变量.py
# @time    : 2019-11-2810:22
# @Author  : zhangshan33
"""
输入两个变量,并相互交换

"""
a = 5
b = 6
print(b,a)

"""
实例
"""
x = input('输入x的值')
y = input('输入y的值')

#创建临时变量
temp = x
x = y
y = temp

print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))