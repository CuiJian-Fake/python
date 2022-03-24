'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/6/2020 5:06 PM
@Software: PyCharm
@File    : day29-SOCKET_Client.py
'''

import socket

Iphone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

Iphone.connect(('127.0.0.1',6666))

while True:

    msg=input('>>>:')
    Iphone.send(msg.encode('utf-8'))

    data=Iphone.recv(1024)

    print('服务器端发来的消息：', data.decode('utf-8').upper())

Iphone.close()


#backlog

 