# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : 17阶乘示例.py
# @time    : 2019-11-2812:58
# @Author  : zhangshan33
"""
所有小于以及等于该数的正整数的积 0 的阶乘为1
"""
n = int(input('输入数'))
f = 1
for i in range(1, n + 1):
    f = f * i
    print(n, f)

"""
实例
"""
# 通过用户输入数字计算阶乘

# 获取用户输入的数字
num = int(input("请输入一个数字: "))
factorial = 1

# 查看数字是负数，0 或 正数
if num < 0:
    print("抱歉，负数没有阶乘")
elif num == 0:
    print("0 的阶乘为 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("%d 的阶乘为 %d" % (num, factorial))