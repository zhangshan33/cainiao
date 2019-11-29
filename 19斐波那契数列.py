# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : 19斐波那契数列.py
# @time    : 2019-11-2816:15
# @Author  : zhangshan33
"""
斐波那契数列
是一组数列0,1,1,2,3,5,8,13
第一个是0 第二个是1
后面都是前两项之和
"""
# 输入要得到的几项数字
n = int(input('需要几项'))
# 固定的第一个数 为0
n1 = 0
# 固定的第二个数 为1
n2 = 1
# 计数,已经有了0,1 所以从2开始
count = 2

print('这是斐波那契数列')
# 先把 0,1 打印出来用','分割
print(n1,',',n2, end=',')

# while循环 输入的数大于2
while count < n:
    # 第三个数=第一个数+第二个数
    n3 = n1 + n2
    # 打印第三个数
    print(n3, end=',')
    # n1 重新赋值 把n2的值给n1
    n1 = n2

    # n2 重新赋值 把n3的值给n1
    n2 = n3
    # 用于后续的前两个数相加

    # 每次count+1
    count += 1

"""
实例
"""
# nterms = int(input("你需要几项？"))
#
# # 第一和第二项
# n1 = 0
# n2 = 1
# count = 2
#
# # 判断输入的值是否合法
# if nterms <= 0:
#     print("请输入一个正整数。")
# elif nterms == 1:
#     print("斐波那契数列：")
#     print(n1)
# else:
#     print("斐波那契数列：")
#     print(n1, ",", n2, end=" , ")
#     while count < nterms:
#         nth = n1 + n2
#         print(nth, end=" , ")
#         # 更新值
#         n1 = n2
#         n2 = nth
#         count += 1
#

n = int(input('项'))
n1 = 0
n2 = 1
count = 2
print('斐波那契数列')
print(n1,',',n2,end=',')
while count < n:
    n3 = n1 + n2
    print(n3,end=',')
    n1 = n2
    n2 = n3
    count += 1
