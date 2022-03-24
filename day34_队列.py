'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/26/2020 4:01 PM
@Software: PyCharm
@File    : day34_队列.py
'''

# import  queue
#
#
# q=queue.Queue()#先进先出 先进后出 优先级 FIFO
#
# q.put(12)
# q.put('hello')
# q.put({'name':123})
#
# while True:
#     data=q.get()
#     print(data)
#     print('=============')

import queue

q=queue.PriorityQueue()

q.put([5,12])
q.put([2,'hello'])
q.put([4,{'name':123}])

while True:
    data=q.get()
    print(data)
    print('=============')