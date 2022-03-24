#!/usr/bin/env python
#coding:utf-8
v=['list',1,1]
for item in range(3,1000):
    v.append(v[item-1]+v[item-2])
print(v)