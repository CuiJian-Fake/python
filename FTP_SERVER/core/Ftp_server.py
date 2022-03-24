'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/19/2020 2:03 PM
@Software: PyCharm
@File    : Ftp_server.py
'''

import socketserver
import socket
import os
import sys
import time
import json

class MyFtp(socketserver.BaseRequestHandler):

    def handle(self):

        while True:
            data=self.request.recv(1024).strip()
            data=json.load(data.decode('utf-8'))
            '''
                {"action":"auth",
                 "username":"yuan",
                 "pwd":123
                 }
            '''

            if hasattr(self,data.get('actoin')):
                func=getattr(self,data.get('actoin'))
                func(**data)

    def auth(self,**data):
        print(data)

        pass
