#!/usr/bin/env python
#coding:utf-8

user_list=[{'name':'alex','password':123},
           {'name':'cb','password':123111},
           {'name':'zz','password':123456},
           {'name':'sb','password':12333},
           ]
current_dic={'name':None,'password':False}
def auth(auth_type='mysql'):
    def auth_func(func):
        print('auth_type is mysql database')
        def wrapper(*args,**kwargs):
            if current_dic['name'] and current_dic['password']:
                return func(*args,**kwargs)
            else:
                username=input('请输入用户名:').strip()
                password=int(input('请输入密码:').strip())
                for user_dic in user_list:
                    if user_dic['name']==username and user_dic['password']==password:
                        current_dic['name']=username
                        current_dic['password']=password
                        res=func(*args,**kwargs)
                        return res
                else:
                    print('用户名密码错误')
        return wrapper
    return auth_func

@auth(auth_type='mysql')
def index():
    print('这是我的主页')
    pass
# @auth_func
# def home():
#     pass
# @auth_func
# def shopping():
#     pass
# @auth_func
# def order():
#     pass

print('beforce--------------->',current_dic)
index()
print('after--------------->',current_dic)