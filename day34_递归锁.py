'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/26/2020 1:58 PM
@Software: PyCharm
@File    : day34_递归锁.py
'''

import threading
import time
class Mythread(threading.Thread):

    def Action_A(self):
        # A.acquire()
        r_lock.acquire()
        print(self.name,"Get A",time.ctime())
        time.sleep(2)


        # B.acquire()
        r_lock.acquire()
        print(self.name,"Get B",time.ctime())
        time.sleep(1)

        # B.release()
        # A.release()
        r_lock.release()
        r_lock.release()

    def Action_B(self):
        # B.acquire()
        r_lock.acquire()
        print(self.name,"Get B",time.ctime())
        time.sleep(2)


        # A.acquire()
        r_lock.acquire()
        print(self.name,"Get A",time.ctime())
        time.sleep(1)

        # A.release()
        # B.release()
        r_lock.release()
        r_lock.release()

    def run(self):
        self.Action_A()
        self.Action_B()




if __name__ == '__main__':

    # A=threading.Lock()
    # B=threading.Lock()
    r_lock=threading.RLock()
    L=[]
    for i in range(5):
        t=Mythread()
        t.start()
        L.append(t)

    for i in L:
        i.join()

    print("Ending==================================>")