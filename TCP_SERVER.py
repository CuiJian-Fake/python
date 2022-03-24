'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/12/2020 5:39 PM
@Software: PyCharm
@File    : TCP_SERVER.py
'''

from socket import  *

TXT=1024
backlog=5
ip_port=('127.0.0.1',6666)

tcp_server=socket(AF_INET,SOCK_STREAM)
tcp_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)#重新使用连接
tcp_server.bind(ip_port)

tcp_server.listen(backlog)

while True:
    print('Server is running')
    conn,addr=tcp_server.accept()
    while True:
        try:
            data=conn.recv(TXT)
            print('======',addr)
            print('Content is',data.decode('utf-8'))
            conn.send(data)
        except ConnectionResetError:
            break
    conn.close()

tcp_server.close()