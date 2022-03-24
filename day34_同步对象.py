'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/26/2020 3:23 PM
@Software: PyCharm
@File    : day34_同步对象.py
'''

import threading
import time

class Boss(threading.Thread):

    def run(self):
        print("BOSS 说 今晚加班==========>")
        event.set()
        time.sleep(5)

        event.set()
        print("BOSS 说 22点下班==========>")

class Worker(threading.Thread):

    def run(self):
        event.wait()
        print("Oh Sad---------------->")
        time.sleep(1)
        event.clear()
        event.wait()
        print("\nOh happy-------------->")
        time.sleep(1)
        event.clear()


if __name__ == '__main__':

    event=threading.Event()
    l=[]
    t=Boss()
    t.start()
    l.append(t)
    for i in range(5):
        t=Worker()
        t.start()
        l.append(t)

    for t in l:
        t.join()

    print("Ending========================>")
