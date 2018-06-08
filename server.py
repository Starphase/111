#!/usr/bin/python 调用/usr/bin下的python解释器
# -*-coding:UTF-8 -*-  声明文件编码
import socket  #头文件

'''创建服务器端程序，用来接收客户端传进的数据'''

from socket import *
from time import ctime	#返回时间

def server():
    HOST = ''  #主机
    PORT = 8000  #设置端口
    ADDR = (HOST,PORT)  #定义端口
    server_socket = socket(AF_INET,SOCK_STREAM) #创建套接字
    server_socket.bind(ADDR) #绑定端口
    server_socket.listen(5) #使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
    while True:
        print 'Waiting for connecting ......'
        tcpclientsocket,addr = server_socket.accept()#如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务器
        print 'Connected by ',addr
        while True:
            data = tcpclientsocket.recv(1024) #接收对方发送过来的数据，最大接收1024个字节
            if not data:
                break  #如果不是字节，程序结束
            print data  #输出字节
            data = raw_input('I>')  ：在字节前加I>
            tcpclientsocket.send('[%s]%s'%(ctime(),data)) #发送一些数据到客户端
        tcpclientsocket.close() #关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
    server_socket.close() # # 关闭监听套接字，只要这个套接字关闭了，就意味着整个程序不能再接收任何新的客户端的连接

server()
