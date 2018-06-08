#!/usr/bin/python  调用/usr/bin下的python解释器
# -*-coding:UTF-8 -*-  声明文件编码
import socket  #头文件

'''创建客户端程序，向服务器传递数据'''

from socket import *

def client():
    HOST = '127.0.0.1' #目标地址
    PORT = 8000  #端口号

    clientsocket = socket(AF_INET,SOCK_STREAM) #创建socket
    clientsocket.connect((HOST,PORT)) #链接服务器
    while True:
    	data = raw_input('>') 
    	if not data:
    		break #没有连接到则中断
    	clientsocket.send(data) #发送数据
    	data = clientsocket.recv(1024) #接收对方发送过来的数据，最大接收1024个字节
    	if not data:
    		break #没有数据则中断
    	print data #输出数据


client()
