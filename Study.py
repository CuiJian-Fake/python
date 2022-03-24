'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/5/2020 11:12 AM
@Software: PyCharm
@File    : Study.py
'''
import time
S=[]

def TT(n):
    for i in range(n,8):
        S.append(i)

def Test():

    for i in range(1,8):
        S.append(i)
        time.sleep(0.1)
       # print(S)
        if len(S)==30:
            return
    Test()

def check():
    a=0
    b=0
    for i in S:
        if i == 6:
            a+=1
        if i == 7:
            b+=1
    if a==5 and b==5:
        print(S[0])
   # if len(S)==30:

        #break
TT(6)
Test()
check()
print(S)