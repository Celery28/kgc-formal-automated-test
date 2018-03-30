"""
测试使用
:author: ronghui.huo <ronghui.huo@kgc.cn>
"""
# def sum_cycle(n):
#
#     sum = 0
#     for i in range(1,n + 1):
#         sum += i
#     return sum
#
#
# def sum_1(number1):
#     sum = 0
#     for i in range(1, number1+1):
#         sum = sum + i
#     return sum
#
# print(sum_1(100))
#
# def sum_recu(n):
#
#     if n > 0:
#         return n + sum_recu(n - 1)
#     else:
#         return 0
#
#
# def sum_2(m):
#     if m > 0:
#         return m + sum_2(m - 1)
#     else:
#         return 0
#
# print(sum_2(100))















# 循环

# def test1(a):
#     if a > 0:
#         sum1 = 0
#         for i in range(1, a+1):
#             sum1 = sum1 + i
#         return sum1
#     else:
#         print("格式错误，请输入正数")
#         a = print(test1(int(input("请重新输入一个字符："))))
#         return a
# print(test1(int(input("请输入一个字符："))))

# # 递归
# def test2(s):
#     if s > 0:
#         return s + test2(s - 1)
#     else:
#         return 0
#         # print(test2(int(input("请重新输入一个正确的字符："))))
# # print(test2(int(input("请输入一个字符："))))
# print(test2(100))
#
#
# def test3(s):
#     if s>0:
#         return s + test3(s - 1)
#     else:
#         return 0
# print(test3(int(input("请输入一个字符："))))
#
# def test4():
#     while True:
#         a = int(input('请输入一个数字,输入END结束：'))
#         if a > 0:
#             sum1 = 0
#             for i in range(1, a + 1):
#                 sum1 = sum1 + i
#             print('sum:{0}'.format(sum1))
#         else:
#             print("格式错误，请输入正数")

# print(test4())
#
#
# def test5():
#     while True:
#         m = input("请输入一个数字，输入end结束运算：")
#         if int(m) >0:
#             sum = 0
#             for i in range(1, m+1):
#                 sum = sum + i
#             print("sum:{0}").format(sum)
#         elif m == "end":
#             break
#         else:
#             print("格式错误，重新输入")
# test5()

# str=[1,2,3,4,5]
# if len(str)==len(set(str)):
#     print("buchongw")
# else:
#     print("dump")
#
#
# str=[1,2,3,4,5]
# for i in  str:
#     for m in str:
#         if i + m == 6:
#             print("这两个数是：{0}和{1}".format(i,m))
#
import requests
import json

url = "http://www.kgc.cn/"
r = requests.get(url)
print(r.headers)
print(r.ok)
print(r.apparent_encoding)
print(json.__all__)


