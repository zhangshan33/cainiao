# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : 10if语句.py
# @time    : 2019-11-2810:36
# @Author  : zhangshan33
"""
使用if...elif...else 判断数字是正数负数或零
"""
a = int(input('输入一个数'))
if a < 0:
    print('这是负数')

elif a == 0:
    print('这是零')

else:
    print('这是正数')

"""
实例
考虑输入范围的判断和异常输出
"""
while True:
    try:
        a = int(input('请输入数'))
        if a < 0:
            print('这是负数')
        elif a == 0:
            print('这是零')
        else:
            print('这是正数')
    except ValueError:
        print('输入无效,请输入数字')
