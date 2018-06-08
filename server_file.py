#-*- coding: UTF-8 -*-  声明文件编码
import SocketServer, time   1.
   
class MyServer(SocketServer.BaseRequestHandler):    
    userInfo = {    
        'panruolin'    : '161001129' }    #设置用户名和密码
   
    def handle(self):    
        print 'Connected from', self.client_address    #显示连接地址
            
        while True:    
            receivedData = self.request.recv(8192)    #最大接收8192个字节
            if not receivedData:    #没接收到则程序继续
                continue   
                
            elif receivedData == 'Hi, server':    #收到相应字符
                self.request.sendall('hi, client')    #回应相应字符
                    
            elif receivedData.startswith('name'):    
                self.clientName = receivedData.split(':')[-1]    
                if MyServer.userInfo.has_key(self.clientName):    
                    self.request.sendall('valid')    
                else:    
                    self.request.sendall('invalid')    
                        
            elif receivedData.startswith('pwd'):    
                self.clientPwd = receivedData.split(':')[-1]    
                if self.clientPwd == MyServer.userInfo[self.clientName]:    
                    self.request.sendall('valid')    
                    time.sleep(5)    
   
                    sfile = open('/home/jd7/ee', 'rb')    #打开ee文件
                    while True:    
                        data = sfile.read(1024)    #传输1024字节
                        if not data:    
                            break   #如果没有文件则中断
                        while len(data) > 0:    
                            intSent = self.request.send(data)    
                            data = data[intSent:]    
   
                    time.sleep(3)    
                    self.request.sendall('EOF')    #文件发送完后发了一个“EOF”，告诉client文件传完了
                else:    
                    self.request.sendall('invalid')    #没传完则发送invalid
                        
            elif receivedData == 'bye':    
                break   
   
        self.request.close()    
            
        print 'Disconnected from', self.client_address    
        print   
   
if __name__ == '__main__':    
    print 'Server is started/nwaiting for connection.../n'    #启动时显示
    srv = SocketServer.ThreadingTCPServer(('localhost', 50000), MyServer)    
srv.serve_forever()            #相当于main函数作用，类的入口
