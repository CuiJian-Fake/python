#!/usr/bin/env python
#coding:utf-8


# # v = ['a','b','c']
# # v1 = ('a','b','c')
# # v2 = {'a','b','c'}
# # dic = {}
# # dic = dict.fromkeys(v2,10)
# # print(dic)
# def si_hi():
#     print('hello')
import os
os.rename('time.py','timmer.py')
TAG=True
while TAG:
    print('level')
    choice=input('level1>>:').strip()
    if choice=='quit':break
    if choice=='exit':TAG=False
    while TAG:
        print('level2')
        choice=input('level2>>:').strip()
        if choice == 'quit': break
        if choice=='exit':TAG = False
        while TAG:
            print('level3')
            choice=input('level3>').strip()
            if choice == 'quit': break
            if choice=='exit':TAG = False