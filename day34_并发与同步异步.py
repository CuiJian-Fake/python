'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/24/2020 2:38 PM
@Software: PyCharm
@File    : day34_并发与同步异步.py
'''

1 同步锁

2 死锁  递归锁

3 信号量和同步对象（了解）

4 队列--生产者消费者模型

5 进程

并发&并行
并发： 是指系统具有处理多任务（动作）能力
并行： 是指系统具有 同时 处理多个任务（动作）能力

同步 与 异步

同步：当一个进程需要接受外部的数据的时候 ------等就同步
                                  ------不等就异步


GIL：全局解释锁 同一时刻只有一个线程被CPU执行

任务：IO密集型 计算密集型
     sleep模拟IO操作
     对于IO密集型的任务 python的多线程是有意义的
     对于计算密集型的任务 python的多线程就不推荐了 采用多进程+协程




