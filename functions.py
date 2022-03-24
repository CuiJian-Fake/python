'''
#-*- coding:utf-8 -*-
@Author:    jcui2x
@Time:      2021/06/01
@Software:  Pycharm
@File:      functions.py
'''

import re


def colors():
 """提取所有的颜色"""
 color_list = []
 with open('colors.txt', 'r', encoding = 'utf-8') as fo:
  for i in fo.readlines():
   ret = re.findall(r"[A-Z][a-z][A-Za-z]*",i) # 提取英文
   color_list += ret # ret得到的是一个列表，相加使得列表合并100
 return color_list



def blesses():
 """提取祝福语"""
 bless_list = []
 with open('blesses.txt', 'r', encoding = 'utf-8') as fo:
  for i in fo.readlines():
   pattern =re.compile(u"[\u4e00-\u9fa5]+") # 提取全部的中文
   result=re.findall(pattern, i)
   bless_list += result
 return bless_list

