'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/18/2020 11:00 AM
@Software: PyCharm
@File    : day31.py
'''
#Server 类：处理链接
#"UnixStreamServer","UnixDatagramServer"，"BaseServer", "TCPServer", "UDPServer"

#request 类：处理通信
#BaseRequestHandler
#StreamRequestHandler
#DatagramRequestHandler

#对于tcp self.request=conn
#对于udp self.request=(data,self.socket udp套接字对象  )


import  socketserver
from functools import partial
import struct #PACK

class Myserver(socketserver.BaseRequestHandler):

    def handle(self):
        print('conn is :',self.request)
        print('addr is :',self.client_address)


        while True:
            try:
                data=self.request.recv(1024)
                if not data:break
                print('收到的信息是：',data)
                self.request.sendall(data)
            except Exception as e:
                print(e)
                break
if __name__ == '__main__':
    s=socketserver.ThreadingTCPServer(('127.0.0.1',8080),Myserver) #线程
    #s=socketserver.ForkingTCPServer(('127.0.0.1', 8080), Myserver) 进程
    s.serve_forever()
