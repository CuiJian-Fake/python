'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/16/2020 3:13 PM
@Software: PyCharm
@File    : day30-UDP-Service.py
'''

from socket import *
import time

ip_port=('127.0.0.1',6666)

udp_client=socket(AF_INET,SOCK_DGRAM)#数据报



while True:

    udp_client.sendto('hello'.encode('utf-8'),ip_port)
    CCC=udp_client.recvfrom(1024)
    print(CCC)
    time.sleep(5)


#recv 在这端缓冲区为空时 就会阻塞
#recvfrom 在这端缓冲区为空时 会收取一个空


