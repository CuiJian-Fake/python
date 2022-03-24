'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/30/2020 5:04 PM
@Software: PyCharm
@File    : day35_生成器.py
'''


def f():
    print("ok")
    s=yield 9
    print(s)
    print('cj')
    yield 8


# print(f().__next__())
gen = f()
# RET=gen.__next__()
# print(RET)
# next(gen)
next(gen)
gen.send(5)
