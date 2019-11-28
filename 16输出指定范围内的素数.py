# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : 16输出指定范围内的素数.py
# @time    : 2019-11-2812:47
# @Author  : zhangshan33
"""
称为质数,出了1和它本身之外不再被其他的除数整除
"""
lower = int(input('最小值'))
upper = int(input('最大值'))

for num in range(lower,upper+1):
    if num >1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)