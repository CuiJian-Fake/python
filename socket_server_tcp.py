'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/16/2020 4:13 PM
@Software: PyCharm
@File    : socket_server_tcp.py
'''

from socket import  *
import subprocess

ip_port=('127.0.0.1',6666)
buffer_size=1024
back_log=5

tcp_server=socket(AF_INET,SOCK_STREAM)
tcp_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)

while True:

    conn,addr=tcp_server.accept()
    while True:

        try:
            Command=conn.recv(buffer_size)
            if not Command:break
            print('收到客户端命令:',Command)
            res=subprocess.Popen(Command.decode('utf-8'),shell=True,
                                 stdout=subprocess.PIPE,
                                 stdin=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            err=res.stderr.read()
            if err:
                cmd_res=err
            else:
                cmd_res=res.stdout.read()
            print('返回命令内容')
            conn.send(cmd_res)
        except Exception as e:
            print(e)
            break
    conn.close()
tcp_server.close()