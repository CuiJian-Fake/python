'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/19/2020 2:28 PM
@Software: PyCharm
@File    : Ftp_client.py
'''
import socket
import optparse
import configparser
import json

class Clienthadler():

    def __init__(self):
        self.op=optparse.OptionParser()
        self.op.add_option("-s", "--s", dest="server")
        self.op.add_option("-P", "--port", dest="port")
        self.op.add_option("-u", "--user", dest="username")
        self.op.add_option("-p", "--password", dest="passwd")

        self.options,self.args=self.op.parse_args()
        self.verify_args(self.options,self.args)
        self.make_connection(self.options)

    def verify_args(self,options,args):
        server=options.server
        port=options.port
        username=options.username
        passwd=options.passwd
        if 0 < int(port) < 65536:
            pass

    def make_connection(self,options):
        self.socke=socket.socket()
        print('====',options.server,options.port)
        self.socke.connect((options.server,int(options.port)))

    def interactive(self):
        if self.auth_check():
            pass


    def auth_check(self):

        if self.options.username is None or self.options.passwd is None:
            username=input("username:")
            password=input("password:")
            return self.get_auth_result(username,password)
        return self.get_auth_result(self.options.username,self.options.passwd)

    def response(self):
        data=self.socke.recv(1024).decode('utf-8')
        data = json.loads(data)
        return data

    def get_auth_result(self,user,passwd):

        data={
            'action':'auth',
            'username':'user',
            'password':'passwd'
        }

        self.socke.send(json.dumps(data).encode('utf-8'))
        response=self.response()
        print(response)










ch=Clienthadler()
ch.interactive()


