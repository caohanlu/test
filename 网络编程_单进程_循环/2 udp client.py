
"""

udp套接字演示

客户端

"""

from socket import *

# 确定服务端地址
ADDR = ('127.0.0.1',8888)

# 创建套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)


# 循环发送、接收消息
while True:
    msg = input(">>")

    if not msg:      # 空字符串,即直接回车，执行break
        break
    if msg == "##":  # 约定了一个特殊的退出指令 ,客户端结束
        break

    udp_socket.sendto(msg.encode(),ADDR)  #字符串变成二进制字节串，给服务端发消息，
    data,addr = udp_socket.recvfrom(1024)
    print("From server:",data.decode())

udp_socket.close()

