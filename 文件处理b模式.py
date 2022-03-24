#!/usr/bin/env python
#coding:utf-8

#f=open('BBB','rb',encoding='utf-8')#rb的方式不能指定编码
# f=open('AAA','rb')
# data=f.read()
# #字符串--》encode---bytes--》--decode-》
# v=data.decode('utf-8')
# print(data)
# print(v)

f=open('BBB','wb')#b的模式不能指定编码
f.write('111111\n'.encode('utf-8'))
f.write(bytes('11111\n',encoding='utf-8'))
f.close()
