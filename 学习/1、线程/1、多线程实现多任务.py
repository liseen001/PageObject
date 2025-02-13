#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc:  https://www.bilibili.com/video/BV1jZ4y1p7zQ?p=248
import threading,time
def dance():
    for i in range(50):
        time.sleep(0.2)
        print("我正在跳舞")


def sing():
    for i in range(50):
        time.sleep(0.2)
        print('我正在唱歌')

#多个任务同时执行：
#python 里执行多人：多线程、多进程、多进程+多线程
# dance()
# sing()

# target 需要的是一个函数，用来指定线程需要执行的任务
t1=threading.Thread(target=dance)  #创建线程1
t2=threading.Thread(target=sing)   #创建线程2

#启动线程
t1.start()
t2.start()