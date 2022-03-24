'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/30/2020 3:42 PM
@Software: PyCharm
@File    : day35_进程池.py
'''

from multiprocessing import Process,Pool
import time,os

def f(i):
    time.sleep(3)
    print(i)
    print(os.getpid())

def bar(arg):
    print("hello")
    print(os.getpid())

if __name__ == '__main__':
    print('main process PID',os.getpid())
    pool=Pool(5)
    for i in range(100):
        # pool.apply_async(func=f,args=(i,))
        pool.apply_async(func=f,args=(i,),callback=bar)#同步
        #回调函数：某个函数或者动作执行成功后 再去执行的函数 就是回调函数
    pool.close()#必须放到join前面
    pool.join()
    print('end===>')