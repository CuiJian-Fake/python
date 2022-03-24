import os
import sys
import re
def test(str):
    if re.findall('[a-zA-Z]',str):
        return '输入不正确'

    ret = re.sub(' ','',str)
    return ret


def level():
    pass

def add():
    pass

def sub():
    pass

def mul(a,b):
    return int(a)*int(b)

def div():
    pass

if __name__ == '__main__':
    str=input('计算器输入>>>')
    # res=re.finditer('\([^()]+\)',str)
    # print(next(res).group())
    # print(next(res).group())
    # print(next(res).group())
    # res=re.findall('[()]',str)#((1-2)-(2-3))
    # print(res)
    ret = test(str)#1+2
    res = re.findall('\d+',ret)
    for i in ret:
        if i == '*':
            v = mul(res[i-1],rest[i+1])

    print(ret)
