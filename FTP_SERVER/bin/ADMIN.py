'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/19/2020 1:50 PM
@Software: PyCharm
@File    : ADMIN.py
'''
import os,sys

PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)

from core import main

# def main():
#     # try:
#         if sys.argv[1] == 'start':
#             Ftp_server.main()
#         else:
#             print('Please USE Python ADMIN.py start')
#     # except Exception:
#     #     print('Please USE Python ADMIN.py start')


if __name__ == '__main__':
    main.ArgvHandler()