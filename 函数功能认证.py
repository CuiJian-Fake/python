#!/usr/bin/env python
#coding:utf-8

def auth_func(func):
    def wrapper(*args,**kwargs):
        username=input('请输入用户名:')
        password=input('请输入密码:')
        if username=='sb' and password=='123':
            res=func(*args,**kwargs)
            return res
        else:
            print('用户名密码错误')
    return wrapper

@auth_func
def index():
    print('这是我的主页')
    pass
@auth_func
def home():
    pass
@auth_func
def shopping():
    pass
@auth_func
def order():
    pass

index()
