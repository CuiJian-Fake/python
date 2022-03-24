#!/usr/bin/env python
#coding:utf-8
#总结   map处理序列中的每个元素，得到一个‘列表’，与原来的序列顺序个数一样
#       filter遍历序列中的每个元素，判断每个元素得到布尔值，如果是True则留下来
people = [{'name':'alex','age':10000},
          {'name':'aaa','age':90000},
          {'name':'bbb','age':100},
          ]

#       reduce处理一个序列 靶序列进行合并操作

print(list(filter(lambda x:x['age']<110,people)))
#       reduce
num_1 = [1,2,15,5,7]
# num_2 = []
#
# for item in num_1:
#     num_2.append(item**2)
#
# print(num_2)
#
# def test(func,n):
#     res = []
#     for i in n:
#         res.append(func(i))
#     return res
# print(test(lambda x:x+1,num_1))

#map()内置函数

#print(map(lambda x:x+1,num_1))
# map(lambda x:x+1,num_1)
# v = map(lambda x:x+1,num_1)
# print(v)
# for item in v:
#     print(item)
#
#print(list(map(lambda x:x+1,num_1)))#可以自己定义函数

# msg = 'efuhakuerhfkgurgha'
#
# print(list(map(lambda x:x.upper(),msg )))

# movie_person = ('sb_alex','aaa_sb','yuanhao')

# for item in movie_person:
#     if 'sb' in item:
#         print(item)

# def filter_test(n):
#     res = []
#     for item in n:
#         if 'sb' in item:
#             #print(item)
#             pass
#         else:
#             res.append(item)
#     return res
# print(filter_test(movie_person))

# def sb_show(n):
#     if 'sb' not in n:
#         return True
# def filter_test(func,movie):
#     res = []
#     for item in movie:
#         if func(item):
#             res.append(item)
#     return res
# # print(filter_test(sb_show,movie_person))
#
# res = (filter_test(lambda x:'sb' not in x,movie_person))
# print(res)

#fiter 函数

# print(list(filter(lambda x:'sb' not in x,movie_person )))

# from functools import reduce
#
# #reduce
#
# v = reduce(lambda x,y:x*y,num_1,10)
# print(reduce(lambda x,y:x*y,num_1,10))