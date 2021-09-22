"""
ftp文件服务客户端
"""
from socket import *
import sys, time

# 服务端地址
ADDR = ("127.0.0.1", 8888)


# 实现具体的请求功能
class FTPClient:
    def __init__(self, sock):
        self.sock = sock

    def do_list(self):
        self.sock.send(b"LIST")  # 发送请求
        result = self.sock.recv(128).decode()  # 回复 字符串
        # 根据回复分情况讨论
        if result == 'OK':
            # 一次性接收文件列表
            file = self.sock.recv(1024 * 1024).decode()
            print(file)
        else:
            print("文件库为空")

    # 下载文件
    def do_get(self, filename):
        data = "RETR " + filename
        self.sock.send(data.encode())  # 发送请求
        # 等回复
        result = self.sock.recv(128).decode()
        if result == 'OK':
            # 接收文件
            f = open(filename, 'wb')
            while True:
                data = self.sock.recv(1024)
                if data == b"##":  # 由于服务端不会退出关闭套接字，所以客户端recv不到空，所以不能if not data，只能这样写##，表示文件发送完了
                    break
                f.write(data)
            f.close()
        else:
            print("文件不存在")

    # 上传文件
    def do_put(self, filename):
        # 本地判断，防止文件路径写错
        try:
            f = open(filename, 'rb')
        except:
            print("该文件不存在")
            return

        # 上传 put 后可能是路径/home/tarena/abc,提取真正的文件名
        filename = filename.split('/')[-1]
        data = "STOR " + filename
        self.sock.send(data.encode())  # 发送请求

        # 等回复
        result = self.sock.recv(128).decode()
        if result == 'OK':
            # 发送文件
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1) #文件发送完后，sleep，再发送##，防止已经发送的文件内容，跟##沾包
                    self.sock.send(b"##")  # 用##表示文件发送完毕，因为客户端套接字不结束的话，服务端recv不到空，就没办法判断文件是不是接受完毕
                    break
                self.sock.send(data)
            f.close()
        else:
            print("文件已经存在")

    # 退出
    def do_exit(self):
        self.sock.send(b"EXIT")  # 告诉服务端，客户端要关闭套接字、结束进程，用于通知服务端关闭对应的客户端连接套接字connfd
        self.sock.close()
        sys.exit("谢谢使用")


def main():
    # 创建套接字
    sock = socket()
    sock.connect(ADDR)

    # 实例化功能类对象
    ftp = FTPClient(sock)

    while True:
        print("============ 命令选项==============")
        print("***           list           ***")
        print("***         get  file        ***")
        print("***         put  file        ***")
        print("***           exit           ***")
        print("==================================")

        cmd = input("请输入命令:")
        if cmd == "list":
            ftp.do_list()
        elif cmd[:3] == "get":
            filename = cmd.split(' ')[-1]  # 提取文件名
            ftp.do_get(filename)
        elif cmd[:3] == "put":
            filename = cmd.split(' ')[-1]  # 提取文件名
            ftp.do_put(filename)
        elif cmd == "exit":
            ftp.do_exit()
        else:
            print("请输入正确命令")


if __name__ == '__main__':
    main()
