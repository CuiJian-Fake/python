#!/usr/bin/env python
#coding:utf-8

f=open('seek.txt','rb')#seek 有三种模式0 1 2 seek 以rb模式 1 2
# print(f.tell())
# f.seek(10)
# print(f.tell())
# f.seek(3)
# print(f.tell())
# f.seek(3,1)#相对于光标的位置3个位置
# print(f.tell())
# f.seek(-4,2)#倒着seek 输出是正序
# print(f.read())
# print(f.tell())
# #写日志一定要加上时间
# #读取文件的最后一行

for i in f:
    offs=-10
    while True:
        f.seek(offs,2)
        data = f.readlines()
        if len(data) > 1:
            #print("123")
            print("文件最后一行为%s" % data[-1].decode('UTF-8'))
            break
        offs *= 2
