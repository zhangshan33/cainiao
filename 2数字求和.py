# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : 2数字求和.py
# @time    : 2019-11-2809:30
# @Author  : zhangshan33

"""
用户输入两个数字，并计算两个数字之和：

"""
# input 输入
a = input('第一个数')
b = input('第二个数')

# 转成int类型 +运算
s = int(a)+int(b)

# f格式化
print(f"第一个数{a}+第二个数{b}={s}")

"""
实例
"""
# 用户输入数字
num1 = input('输入第一个数字：')
num2 = input('输入第二个数字：')

# 求和
sum = float(num1) + float(num2)

# 显示计算结果
print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))