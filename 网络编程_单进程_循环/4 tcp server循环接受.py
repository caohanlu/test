"""
tcp 服务端循环模型1

重点代码

"""

from socket import *

# 创建tcp套接字 (默认也是tcp)
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(('0.0.0.0',8888))

# 设置监听
tcp_socket.listen(5)


# 循环等待、处理、客户端连接【跟一个客户单之间，消息收发完了后，才能跟另一个客户端建立tcp三次握手】
while True:
    print("Waiting for connect...")
    connfd,addr = tcp_socket.accept()   # tcp三次握手，生成该客户端的连接套接字
    print("Connect from",addr)          # 打印客户端地址

    # 与该客户端之间循环收发消息,
    # 跟这个客户端交互消息时，另一个客户端是没办法跟服务器交互消息的,因为代码进入内层循环了，没办法执行到外层循环的accept
    while True:
        data = connfd.recv(1024)
        if not data:    # 另外一端不存在了，recv会返回空【即一端close了，另一端recv会返回空，而不是通过网络发来一个空】
            break
        print("Recv:",data.decode())
        connfd.send(b"Thanks#")

    connfd.close()      # 该客户端close了，则服务端关闭对应的连接套接字后，进入外层循环，等待另一个客户端connect来accept三次握手建立连接

# 关闭
tcp_socket.close()



