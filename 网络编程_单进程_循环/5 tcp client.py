"""
练习1：  使用tcp完成 模拟客服机器人对话
小美    你多大了 --》 我2岁啦；
       你是男生女生 --》 我是机器人，没有性别之分啦
       xxx --> xxxxx

从客户端可以不断的发送问题，小美会将回答发送回答打印，如果你的问题
它听不懂则回复 "人家还小不太明白"。
"""

from socket import *

# 创建tcp套接字
tcp_socket = socket()

# 发起连接 连接服务端
tcp_socket.connect(("127.0.0.1",8888))

# 发送消息
while True:
    msg = input("我：")
    if not msg:
        break
    tcp_socket.send(msg.encode()) # 发送字节串
    data = tcp_socket.recv(1024)
    print("小美:",data.decode()) # 转换字符串

tcp_socket.close()
