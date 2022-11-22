# --*-- coding:utf-8 --*-
 
from socket import *
from threading import Thread
 
class TcpServer(object):
    """Tcp服务器"""
    def __init__(self, Port):
        """初始化对象"""
        self.code_mode = "utf-8"    #收发数据编码/解码格式
        self.server_socket = socket(AF_INET, SOCK_STREAM)   #创建socket
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)   #设置端口复用
        self.server_socket.bind(("", Port))     #绑定IP和Port
        self.server_socket.listen(100)  #设置为被动socket
        print("Listen...")
 
    def run(self):
        """运行"""
        while True:
            client_socket, client_addr = self.server_socket.accept()    #等待客户端连接
            print " %s online" % client_addr[0]
 
            tr = Thread(target=self.recv_data, args=(client_socket, client_addr))   #创建线程为客户端服务
            tr.start()  #开启线程
 
        self.server_socket.close()
 
    def recv_data(self, client_socket, client_addr):
        """收发数据"""
        while True:
            data = client_socket.recv(1024).decode(self.code_mode)
            if data:
                print("%s:%s" % (client_addr[0], data))
                client_socket.send(data.encode(self.code_mode))
            else: 	#客户端断开连接
                print("%s offline" % (client_addr[0]))
                break
 
        client_socket.close()
 
def main():
    port = int(raw_input("请输入要绑定的Port:"))
    my_server = TcpServer(port)
    my_server.run()
 
if __name__ == "__main__":
    main()
