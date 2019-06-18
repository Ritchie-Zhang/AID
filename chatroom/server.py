#!/usr/bin/env python3
#coding=utf-8

'''
name:   ChenChuan
email:  xiaoganzcc@163.com
date:   2019-6
class:  AID
introduce: Chatroom server
env : python3.5
'''

from socket import *
import os
import sys

#接收客户端请求
def do_parent():
    print("do parent")

#做管理员喊话
def do_child():
    print("do child")
# 创建网络，创建进程，调用功能函数
def main():
    #server address
    ADDR = ('0.0.0.0', 8888)

    #创建套接字
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)

    #创建一个单独的进程处理管理员喊话功能
    pid = os.fork()
    if pid < 0:
        sys.exit("创建进程失败")
    elif pid == 0:
        do_child()
    else:
        do_parent()

if __name__ == "__main__":
    main()