# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : 11判断字符串是否是数字.py
# @time    : 2019-11-2810:49
# @Author  : zhangshan33

# isdigit 方法监测字符串是否只由数字组成
s = '124呵呵3'
if s.isdigit():
    print('True')

else:
    print('False')

# isnumeric 方法监测字符串是否只由数字组成 针对Unicode对象
c = '34呵呵'
if c.isnumeric():
    print('True')

else:
    print('False')


# 函数
def is_number(s1):
    try:
        float(s1)
        return True
    except ValueError:
        return False


print(is_number('22'))


# 函数
def is_number2(s2):
    if s2.isdigit():
        return True
    else:
        return False


print(is_number2('tt11'))
