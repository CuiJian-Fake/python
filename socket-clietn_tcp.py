'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/16/2020 4:14 PM
@Software: PyCharm
@File    : socket-clietn_tcp.py
'''

from socket import *
import subprocess

ip_port=('127.0.0.1',6666)

tcp_client=socket(AF_INET,SOCK_STREAM)
tcp_client.connect(ip_port)

while True:

    Command=input('>>>:')
    if Command == 'quit':break
    tcp_client.send(Command.encode('utf-8'))
    Command_res=tcp_client.recv(1024)
    print('输出结果:',Command_res.decode('gbk'))

tcp_client.close()