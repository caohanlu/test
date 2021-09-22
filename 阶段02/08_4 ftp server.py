"""
ftp 文件服务 服务端
多线程并发模型训练
"""

from socket import *
from threading import Thread
import os, time

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)  # 服务器地址

# 文件库
FTP = "/root/Pictures/"


# 处理客户端请求
class FTPServer(Thread):
    def __init__(self, connfd):
        super().__init__()
        self.connfd = connfd

    def do_list(self):
        # 判断文件库是否为空
        file_list = os.listdir(FTP)
        if not file_list:
            self.connfd.send(b'FAIL')  # 列表为空
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)  # ok后面sleep,防止ok跟后面的大字符串沾包
            data = "\n".join(file_list)  # 把列表元素通过换行，拼接成大字符串，一次性发送，这样就不怕沾包了
            self.connfd.send(data.encode())

    # 处理下载
    def do_get(self, filename):
        try:
            f = open(FTP + filename, 'rb')
        except:
            # 文件不存在,报异常
            self.connfd.send(b"FAIL")
            return
        else:
            # 文件打开成功
            self.connfd.send(b"OK")
            time.sleep(0.1)  # 防止ok跟后面发送的文件内容沾包
            # 发送文件
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)  #防止下面的##跟已经发送的文件沾包
                    self.connfd.send(b"##")  # 通知客户端，文件发送完毕
                    break
                self.connfd.send(data)
            f.close()

    # 处理上传
    def do_put(self, filename):
        if os.path.exists(FTP + filename):  # 判断文件是否存在，即是否已经上传过了
            self.connfd.send(b"FAIL")
            return
        else:
            self.connfd.send(b"OK")
            # 接收文件
            f = open(FTP + filename, 'wb')
            while True:
                data = self.connfd.recv(1024)
                if data == b"##":
                    break
                f.write(data)
            f.close()

    # 作为一个线程内容处理某一个客户端的请求
    def run(self):
        # 总分模式
        while True:
            # 某个客户端所有的请求
            data = self.connfd.recv(1024).decode()
            print("Request:", data)  # 调试
            # 更具不同的请求做不同处理
            if not data or data == 'EXIT':  # 客户端异常退出关闭套接字，则recv空字节穿，或者客户端输入exit，则服务端关闭这个客户端的连接套接字connfd
                self.connfd.close()
                return
            elif data == 'LIST':
                self.do_list()
            elif data[:4] == 'RETR':  # 提取文件名
                filename = data.split(' ')[-1]
                self.do_get(filename)
            elif data[:4] == 'STOR':
                filename = data.split(' ')[-1]
                self.do_put(filename)


def main():
    # tcp套接字创建
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    print("Listen the port %s" % PORT)

    # 循环连接客户端
    while True:
        try:
            connfd, addr = sock.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            sock.close()
            return
        # 为连接进来的客户端创建单独的线程
        t = FTPServer(connfd)  # 使用自定义线程类创建线程,start后，执行run函数，在run函数里进行总--分
        t.setDaemon(True)  # 主线程退出，分之线程终止服务
        t.start()


if __name__ == '__main__':
    main()
