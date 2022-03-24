'''
#-*- coding:utf-8 -*-
@Author:    jcui2x
@Time:      2021/06/01
@Software:  Pycharm
@File:      61_children_day.py
'''

import tkinter as tk
import random
import threading  # 使用多线程
import time
import functions  # functions是自己建立的一个Python文件，后面会简单介绍一下


def dow():
    color_list = functions.colors()
    font_list = ['黑体', '宋体', '仿宋', '微软雅黑', '楷体', '隶书', '华文琥珀', '幼圆', '华文行楷', '新宋体']
    text_list = functions.blesses()
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('来自阿健的六一祝福')  # 一雄是我的名
    window.geometry("300x100" + "+" + str(a) + "+" + str(b))
    tk.Label(window,
             text=random.sample(text_list, 1),  # 标签的文字
             bg=random.sample(color_list, 1),  # 背景颜色
             font=(random.sample(font_list, 1), 17),  # 字体和字体大小
             width=20, height=20  # 标签长宽
             ).pack()  # 固定窗口位置
    window.mainloop()


def bless(x):
    threads = []
    for i in range(x):  # 需要的弹框数量
        t = threading.Thread(target=dow)
        threads.append(t)
        time.sleep(0.1)
        threads[i].start()


def main():
    num = int(input('请输入需要的祝福数量：'))
    bless(num)


if __name__ == '__main__':
    main()