'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/12/2020 4:17 PM
@Software: PyCharm
@File    : 时间.py
'''

import time

# print(time.localtime())
# print(time.time())#显示时间戳
# print(time.localtime(time.time()))
print(time.gmtime(time.time()+28800))
print(time.mktime(time.localtime()))
print(time.strftime('%Y-%m-%d %X',time.localtime()))


