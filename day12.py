#!/usr/bin/env python
#coding:utf-8

#字符串创建后不可以修改的
#列表有序 元素可以修改
# v = "alex"
# #v = 1
# v = v.replace('le','1')
# print(v)
#
# #元祖 是有序的
# tuple
# #元祖不可以被修改 不能被增加或者删除
# tu = (111,22,33,44,)
# #一般写元祖的时候推荐在最后加上,
#元祖的一级元素不可以被修改

#count 出现次数
#index出现位置

# tu = (111,'alex',(11,22),[(22,44)],True,33,44,)
# tu[3].append(10)
# print(tu)

#######################################字典##############################3

dict

info ={"k2":"v1","k2":"v2"}#键值对

#字典的value可以是任意值
#字典的key可以是数字可以是字符串可以是元组
#字典是无序的
#键值重复只保留一个
#del info['k1']
# for item in info:
#     print(item)
# for item in info.keys():
#     print(item)
# for item in info.values():
#     print(item)
# for item in info.items():
#     print(item)
#print(info['k1'])

#dic
# v = dict.fromkeys([123,456],111)
# print(v)

# 根据key取默认值 get('k1',1111)不存在返回1111
#
# v = info.get('k1','haha')
# print(v)

#popitem 随即删除key value pop 指定key删除

# v = dic.setdefault('k1','1234')#存在的key则不设置 不存在的key 则value为1234
#
# dic.update(k1=123,k2=456)

#################################整理#########################

#一 数字
#int（）

#二 字符串
#replace/find/join/strip/startswith/split/upper/lower/format

#三 列表
#append extend insert

#四 元组
#忽略
#索引 切片 循环 #以及元素不能被修改

#五 字典
#get/update/key/value/items
#for,索引
dic = {'k1':123}
v = 'k1' in dic
print(v)

