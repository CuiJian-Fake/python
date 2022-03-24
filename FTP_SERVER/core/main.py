'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/19/2020 2:48 PM
@Software: PyCharm
@File    : main.py
'''
import optparse
import socketserver
from core import Ftp_server
from conf import settings

class ArgvHandler():


    def __init__(self):
        self.op=optparse.OptionParser()

        self.op.add_option("-s","--s",dest="server")
        self.op.add_option("-P", "--port", dest="port")

        opta,args=self.op.parse_args()
        print(opta)
        print(args)

        self.verify_args(opta,args)

    def verify_args(self,opta,args):

        cmd=args[0]

        if hasattr(self,cmd):
            func=getattr(self,cmd)
            func()

    def start(self):
        print('=========FTP SERVER IS RUNNING========')
        s=socketserver.ThreadingTCPServer((settings.IP,settings.PORT),Ftp_server.MyFtp)
        s.serve_forever()

    def help(self):
        pass

