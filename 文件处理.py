#!/usr/bin/env python
#coding:utf-8

# r w a
# f = open('chenli.txt','r',encoding='utf-8')#文件句柄
# # data = f.read()
# # print(data)
# print(f.readable())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readlines())
# f.close()
# # f = open('xxx')
# data = f.read()
# print(data)

# f = open('chenli1.txt','w',encoding='utf-8')#文件句柄
# f.write('aaa\nbbb\nccc\n\tdddddddd\n')
# f.writelines(['666\n','777\n'])#写的参数只能是字符串 不能是其他的东西
# f.close()

# f = open('chenli1.txt','a',encoding='utf-8')#文件句柄
# f.write('写到文件最后')
# f.close()

# f=open('xxx','r+',encoding='utf-8')
# data=f.read()
# print(data)
# f.write('牛逼')
# f.write('sb')
# f.close()

src_f = open('xxx','r',encoding='utf-8')
data=src_f.readlines()
src_f.close()

dst_f=open('xxx_new','w',encoding='gbk')
dst_f.write(data[0])
dst_f.close()

with open('xxx','w') as f:
    f.write('aaa')
with open('xxx','r',encoding='gbk') as src_a,\
    open('xxx_new','w',encoding='utf-8') as dis_a:
    data=src_a.read()
    dis_a.write(data)