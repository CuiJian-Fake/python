'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/19/2020 2:27 PM
@Software: PyCharm
@File    : ADMIN.py
'''

import sys

def main():
    # try:
        if sys.argv[1] == 'start':
            print('START')
        else:
            print('Please USE Python ADMIN.py start')
    # except Exception:
    #     print('Please USE Python ADMIN.py start')

if __name__ == '__main__':
    main()