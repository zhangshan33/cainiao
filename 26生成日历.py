# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : 26生成日历.py
# @time    : 2019-11-2821:54
# @Author  : zhangshan33

"""
生成指定的日期的日历
导入日历模块 calendar
"""
import calendar

y = int(input('年份'))
m = int(input('月份'))
print(calendar.month(y,m))