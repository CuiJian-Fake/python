'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/5/2020 2:30 PM
@Software: PyCharm
@File    : day29.py
'''

property

#type()可以实例化一个类 metaclass

#错误 语法错误 逻辑错误
#异常  程序运行错误发出的

try:
    age=input('>>>:')
    int(age)
except ValueError:
    print('NO')

#万能异常

except Exception:
    print('YES')

else:
    print('没有异常执行我')

finally:
    print('不管是否有异常我都执行')

try:
    raise  主动触发异常
except Exception:
    print("raise")

#可以自定义类

#断言

assert 1==2  #判断 可以用if代替

#什么时候用异常处理那

