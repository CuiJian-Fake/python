#!/usr/bin/env python
#coding:utf-8

# num = "0011"
# v = int(num,base=8)
# print(v)
#
# # test = "alexalex"
# # v = test.find("ex",5,8) #大于等于5小于8找位置
# # print(v)
#
# test = "i am {name}" #格式化 讲一个字符串占位符替换为指定值
# print(test)
# v=test.format(name='alex')
# print(v)

#format_map({"name":11,"hehe":22})
#index 找不到报错 自动忽略

# s = "aishfiaehife\t00iejdiajed" #expandtabs 断句20
# v = s.expandtabs(20)
# print(v)

# test = "as2df"
# v = test.isalpha()#判断输入的是否是字母
# print(v)

# test = "123"
# v1 = test.isdecimal()#特殊数字不支持
# v2 = test.isdigit()#特殊数字支持②
# v3 = test.isnumeric()#字节判断
# print(v1,v2)

# test = "_123"
# v = test.isidentifier()#判断标识符
# print(v)

# test  = "aiejfoiaejf"
# v =  test.isprintable()#是否存在不可见的字符
# print(v)

#isspace()是否全部是空格

#title 标题首字母大写 istitle 判断标题首字母是否大写
# test = "Return True if the string is an alpha-numeric string, False otherwise."
# v1 = test.istitle()
# print(v1)
# v2 = test.title()
# print(v2)
# v3 = v2.istitle()
# print(v3)

#join 将字符串中的每个元素按照指定的分隔符进行拼接

# test = "你是风儿我是沙"
# print(test)
# t = '_'
# v = t.join(test)
# print(v)
#
# test = "alex"
# v = test.ljust(20,'*')
# print(v)
#
# test = "alex"
# v = test.rjust(20,'*')
# print(v)

#判断小写 改成小写
# test = "Alex"
# v1 = test.lower()
# print(v1)
#
# v2 = v1.islower()
# print(v2)

# test = "alex"
# v1 = test.upper()
# print(v1)
#
# v2 = v1.isupper()
# print(v2)

#去除空白 \t \n 去除指定内容 有限最多匹配
# test = "    alex   "
# v1 = test.strip()
# print(v1)
# v2 = test.lstrip()
# print(v2)
# v3 = test.rstrip()
# print(v3)

# test = "asdfg"
# test1 = "12345"
#
# v = "aefesgheks:fdfgdsdgklsdfdf:sdfsd"
# m = str.maketrans(test,test1)
# new_v = v.translate(m)
# print(new_v)

#partition 只能划分三部分
# test = "tetaesfaefaefaefsfsd"
# # v = test.partition('s')
# # v1 = test.rpartition('s')
# # print(v,v1)
#
# #split 也是分割 但是不能找到分割的东西 数字次数 1 一次 2两次
# v = test.split('s',1)
# print(v)

#分割True保留换行 False不保留
# test = "adfadsfdf\nafawefae\naweaweaw"
# v = test.splitlines(True)
# print(v)

# test = "aLex"
# v = test.swapcase()#大小写转换
# print(v)

# test = "alexalexalex"
# v = test.replace('ex','bbb',1)#替换1替换第一个2替换前2个
# print(v)
################################################上面6个基本魔法
# join
# split
# find
# strip
# upper
# lower
#replace

###############################################灰魔法

test = "证件分"
# #索引 下标
# v = test[3]
# print(v)

#切片
# v = test[0:2]
# print(v)
#
# #len
# v = len(test)
# print(v)#python2.7 9 一个汉字3个字节
#
# for i in test:
#     print(i)

##################################深灰魔法
#字符串一旦穿件不可修改 一旦修改 或者 拼接 那都是重新生成字符串

# v = range(100)
# print(v)
#
# v1=[]
# for item in v:
#     v1.append(item)
# print(v1)

# test = input(">>>")
#
# i = 0
# for item in test:
#     print(i)
#     i = i + 1 #用了 len

#列表
# del li[1]
# #支持for while 循环

# li = [1,12,9,"age",[1,2,3],"alex",True]
# v1 = "2" in li
# print(v1)
#字符串转换列表 list(字符串 内部使用for循环)
# s = "aefhaehlgiaehgiuaerghkauregha"
# new_li = list(s)
# print(new_li)

#####################列表中如果只有字符串可以直接拼接 如果有数字需要for循环

#list类的一个对象
li = [11,22,33,44]
#参数
# v = li.append(5)#不需要v直接在原值上改变
# print(v)
# print(li)

#li.clear()#清空
# v = li.copy()#浅拷贝
# print(v)
#
# v = li.count(22)#计算元素的次数
# print(v)
#
# li.extend([9988,"aaa"])#for i in
# print(li)
# list
# v = li.index(22)#找到最近一个 最左边优先
# print(v)
#
# v = li.pop(1)#删除某个值 并获取 后面数字某个索引的值
# print(v)

li.remove(22)#最左删除
print(li)

li.reverse()#当前列表进行翻转
print(li)

li.sort(reverse=True)#排序
print(li)



##############################深灰魔法 list 类中的方法

#append








