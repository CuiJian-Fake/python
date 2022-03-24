'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/16/2020 3:13 PM
@Software: PyCharm
@File    : day30-UDP-Service.py
'''

from socket import *

ip_port=('127.0.0.1',6666)

udp_server=socket(AF_INET,SOCK_DGRAM)#数据报

udp_server.bind(ip_port)

while True:

    data=udp_server.recvfrom(1024)
    print(data)
    udp_server.sendto(data[0],data[1])

