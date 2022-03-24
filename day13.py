#!/usr/bin/env python
#coding:utf-8

# l1 = [11,22,33]
# l2 = [22,33,44]
# l3 = []
# for item in l1:
#     print(item)
#     if item in l2:
#       l3.append(item)
#
# print(l3)


# i = 0
# for item in range(1,9):
#
#     for item1 in range(1 ,9):
#         v = str(item) + str(item1)
#         i += 1
#         print(v)
# print(i)

#99乘法表

# i = 1
# for item in range(i,10):
#     i = i + 1
#     for item1 in range(1,i):
#         v = item * item1
#         print(v,"=",item,"*",item1,end='\t')
#
#     print('\n')

#20

#公鸡5文钱1只 母鸡3文钱1只 小鸡三只1文钱 用100文钱买100只鸡

#a + b +  c = 100
#5*a + 3*b + (c/3) = 100
# for a in range(1,101):
#     for b in range(1, 101):
#         for c in range(1, 101):
#             if (a + b + c == 100) and (5 * a + 3 * b + (c / 3) == 100):
#                 print(a,b,c)

# li = ['aele','eric',123]
# l1 = [] #li[2] = str(li[2])
# for item in li:
#     st = str(item)
#     l1.append(st)
# v = '_'.join(l1)
# print(v)

tu = ('alex','eric','rain',)
# for item in tu:
#     print(item)
# v = len(tu)
# print(v)

enumerate #返回索引和值从10开始

# for inde,item in enumerate(tu,10):
#     print(inde,item)

# tu = ("alex",[11,22,{"k1":'v1',"k2":["age","name"],"k3":(11,22,33)},44],)
#  #tu[1][2]['k2'].append('Seven')
# print(tu)

# nums = [2,7,11,15,1,8,7]
# li = []
# for item in nums:
#     for item1 in nums:
#         if 9 == item + item1:
#             print(item,item1)
#             li.append((item,item1))
#             print(li)

user_list = []
for i in range(1,302):
    temp = {'name':'alex'+str(i),'email':'alex@lve.com','pwd':'pwd'+str(i)}
    user_list.append(temp)

print(user_list)

while True:
    a = input("请输入要查看的页码>>>")
    try:
        if int(a):
            v = int(a)
            if v >= 31:
                print(user_list[300])
            else:
                for i in range(v*10-10,v*10):
                    print(user_list[i])
                    print("页码最大31页")
        # else:
        #     print('输入内容格式错误 请重新输入')
    except ValueError:
        print('输入内容格式错误 请重新输入')

