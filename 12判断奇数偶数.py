# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : 12判断奇数偶数.py
# @time    : 2019-11-2811:11
# @Author  : zhangshan33

"""
判断一个数是奇数还是偶数
"""
n = int(input('请输入一个数'))
if n % 2 == 1:
    print('奇数')
else:
    print('偶数')

# 三元运算
print('奇数' if n % 2 == 1 else '偶数')
