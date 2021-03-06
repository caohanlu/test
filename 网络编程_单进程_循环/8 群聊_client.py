"""
chat client
发送请求，得到结果
"""
from socket import *
from multiprocessing import Process
import sys

# 服务端地址
ADDR = ("0.0.0.0", 8000)


# 请求进入聊天室 OK FAIL
def login(sock):
    while True:
        name = input("Name:")
        msg = "L " + name  # 根据通信协议整理发送信息
        sock.sendto(msg.encode(), ADDR)  # 发送请求
        result, addr = sock.recvfrom(128)  # 等待回复
        if result.decode() == 'OK':
            print("您已进入聊天室")
            return name
        else:
            print("你的名字太受欢迎了，换一个吧")


# 接收消息
def recv_msg(sock):
    while True:
        data, addr = sock.recvfrom(2048)
        print("\n" + data.decode() + "\n我：", end="")


# 发送消息
def send_msg(sock, name):
    while True:
        try:
            msg = input("我:")
        except KeyboardInterrupt:
            msg = "exit"
        if msg == 'exit':
            data = "E " + name
            sock.sendto(data.encode(), ADDR)
            sys.exit("您已退出聊天室")
        data = "C %s %s" % (name, msg)
        sock.sendto(data.encode(), ADDR)


def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    # sock.bind(('0.0.0.0',55555))     # 因为udp是无连接的，所以客户端服务器如果长时间不收发消息，则客户端的端口也可能变化，
                                     # 而服务端记录的还是变化之前的端口，所以客户端也把端口固定下来
    name = login(sock)  # 进入聊天室

    # 为聊天创建子进程
    p = Process(target=recv_msg, args=(sock,))
    p.daemon = True  # 父进程退出子进程也退出
    p.start()
    send_msg(sock, name)


if __name__ == '__main__':
    main()

