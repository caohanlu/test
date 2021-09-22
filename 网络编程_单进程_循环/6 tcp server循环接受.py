"""
tcp 服务端循环模型 2

重点代码
"""

from socket import *

# 创建tcp套接字 (默认也是tcp)
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(('0.0.0.0',8888))

# 设置监听
tcp_socket.listen(5)

# 循环等待处理客户端连接
#如果每个客户端收发完消息后，都断开tcp连接，所以可以接受另一个客户端accept建立连接，
#如果每个客户端收发的消息很少，则处理速度很快，在直观感受上，服务端可以同时接受多个客户端的收发消息了
#一般网页就是这种网络模型
print("处理客户端消息")
while True:
    connfd,addr = tcp_socket.accept() # 客户端三次握手建立连接
    print("Connect from",addr) # 打印客户端地址
    data = connfd.recv(1024)
    print("Recv:",data.decode())
    connfd.send(b"Thanks")
    connfd.close() # 某个客户端退出对应的连接套接字就没用了

# 关闭
tcp_socket.close()


