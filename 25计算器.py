# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : 25计算器.py
# @time    : 2019-11-2821:40
# @Author  : zhangshan33
"""
实现加减乘除
"""


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# 用户输入
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")

choice = input('选择(1/2/3/4)')
n1 = int(input('第一个数'))
n2 = int(input('第二个数'))

if choice == '1':
    print(n1, "+", n2, "=", add(n1, n2))
elif choice == '2':
    print(n1, "-", n2, "=", subtract(n1, n2))
elif choice == '3':
    print(n1, "*", n2, "=", multiply(n1, n2))
elif choice == '4':
    print(n1, "/", n2, "=", divide(n1, n2))
else:
    print('请选择1.2.3.4')