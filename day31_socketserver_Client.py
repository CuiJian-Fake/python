'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/18/2020 2:11 PM
@Software: PyCharm
@File    : day31_socketserver_Client.py.py
'''

import socket

Iphone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Iphone.connect(('127.0.0.1', 8080))

while True:
    msg = input('>>>:')
    Iphone.send(msg.encode('utf-8'))

    data = Iphone.recv(1024)

    print('服务器端发来的消息：', data.decode('utf-8').upper())

Iphone.close()

# backlog

