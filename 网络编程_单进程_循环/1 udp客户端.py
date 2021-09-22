
'''

服务端要先执行，
因为客户端，是要访问服务端的ip、端口的，
所以服务端要先跑起来

'''


from socket import *

# 确定服务端地址
ADDR = ('127.0.0.1',8888)

# 创建套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 循环发送接收消息
while True:
    # 输入单词
    word = input(">>")
    if not word:
        break
    # 发送单词
    udp_socket.sendto(word.encode(),ADDR)
    data,addr = udp_socket.recvfrom(1024)   #这里会一直等待接受服务端发来的消息，如果服务端不发来消息，就会一直等待
    print("%s:%s"%(word,data.decode()))     #打印查询的单词、以及从服务端接受的单词的解释

print("退出程序")
udp_socket.close()



