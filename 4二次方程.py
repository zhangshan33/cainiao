# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : 4二次方程.py
# @time    : 2019-11-2809:50
# @Author  : zhangshan33

"""
二次方程式 ax**2 + bx + c = 0
a、b、c 用户提供，为实数，a ≠ 0
"""
# cmath 模块 数学运算

import cmath

a = float(input('第一个数'))
b = float(input('第二个数'))
c = float(input('第三个数'))

# 计算
d = (b ** 2) - (4 * a * c)

# 求解
e = (-b - cmath.sqrt(d)) / (2 * a)

print(d)

"""
实例
"""
import cmath

a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))

# 计算
d = (b ** 2) - (4 * a * c)

# 两种求解方式
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print('结果为 {0} 和 {1}'.format(sol1, sol2))
