# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : 15质数判断.py
# @time    : 2019-11-2812:40
# @Author  : zhangshan33
"""
质数 大于1的自然数 除了1和它本身外,不能被其他自然数整除
"""
n = int(input('请输入'))
if n > 1 and n%n == 0 :
    print('质数')

"""
示例
"""
# 用户输入数字
num = int(input("请输入一个数字: "))

# 质数大于 1
if num > 1:
    # 查看因子
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "不是质数")
            print(i, "乘于", num // i, "是", num)
            break
    else:
        print(num, "是质数")

# 如果输入的数字小于或等于 1，不是质数
else:
    print(num, "不是质数")