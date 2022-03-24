'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/6/2020 4:53 PM
@Software: PyCharm
@File    : day29-SOCKET_Service.py
'''

import socket

Iphone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

Iphone.bind(('127.0.0.1',6666))

Iphone.listen(5)
print('---------->')

link,addr=Iphone.accept()

message=link.recv(1024)

print('客户端发来的消息:',message,addr)

link.send(message)

link.close()

Iphone.close()
