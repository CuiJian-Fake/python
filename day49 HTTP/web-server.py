'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 4/7/2021 10:58 AM
@Software: PyCharm
@File    : web-server.py
'''

from wsgiref.simple_server import make_server

def application(environ,start_response):

    # print("path",environ["PATH_INFO"])
    path=environ["PATH_INFO"]
    start_response('200 OK',[('Content-Type','text/html')])

    if path=="/cj":

        return [b'<h1>Hello cj!</h1>']
    elif path=="/cj1":

        return [b'<h1>Hello cj1!</h1>']

    else:
        return [b'<h1>404</h1>']

    #return [b'<h1>Hello ok!</h1>']

httpd = make_server('',8080,application)

print(('Serving HTTP on port 8080...'))

httpd.serve_forever()