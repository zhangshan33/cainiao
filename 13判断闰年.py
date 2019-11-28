# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : 13判断闰年.py
# @time    : 2019-11-2811:36
# @Author  : zhangshan33
"""
润年 输入一个数字
除以4余0
除以100余0
除以400余0
"""
n = int(input('请输入'))
if n % 4 == 0:
    if n % 100 == 0:
        if n % 400 == 0:
            print('润年')
        else:
            print('不是润年')
    else:
        print('不是润年')
else:
    print('不是润年')

# 或与非运算
if (n % 4) == 0 and (n % 100) == 0 and (n % 400) == 0:
    print('闰年')
else:
    print('不是闰年')

# 第三方calendar库中的isleap()方法 只能判断能被4整除

import calendar

m = calendar.isleap(n)
if m == True:
    print('闰年')
else:
    print('不是闰年')

# isleep判断能被4整除
l = int(input("请输入数字"))
l2 = calendar.isleap(l)
print(l2)
