"""

udp_server.py

udp套接字编程演示


"""


from socket import *


# 创建udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 确定服务器地址
ADDR = ('0.0.0.0',8888)

# 绑定地址
udp_socket.bind(ADDR)

while True:#由于实验里收发的数据很小，服务端处理的速度很快，所以即使有多个终端跟服务器收发消息，现象上看，好像是支持多客户端同时跟服务端交互
           #如果跟一个客户端收发消息很慢，则此时是没办法跟另一个客户端收发消息的
    msg,addr = udp_socket.recvfrom(1024)    # 接收客户端消息

    # if msg == b'##':              # 与客户端约定了一个特殊的退出指令 ,
    #     break                     # 但是服务端程序一般不退出, 因为不可能因为一个客户端程序退出，而服务端程序也退出，所以这段代码一般不写
    #
    print("Recv:",msg.decode())

    udp_socket.sendto(b"Thanks",addr) # 给对应客户端发送消息,
                                    # 这里的addr就是上面msg,addr = udp_socket.recvfrom(1024)里获取的客户端地址、端口

udp_socket.close()


