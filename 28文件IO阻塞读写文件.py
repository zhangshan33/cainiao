# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : 28文件IO阻塞读写文件.py
# @time    : 2019-11-2822:18
# @Author  : zhangshan33

"""

操作文件 open
文件操作

"""
with open('readme.txt','w')as f:
    f.write('这是写文件的操作')

with open('readme.txt','r',)as f:
    text = f.read()
print(text)