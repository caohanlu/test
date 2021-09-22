'''


从客户端指定一张图片，将其传输到服务端
在服务端以日期为图片名称存储

比如： 客户端有一张  xxxxx.jpg
     传到服务端存为 2020-7-10.jpg

'''



"""
思路：
1. 创建套接字
2. 连接服务端
3. 读取图片内容
4. 发送图片内容
5. 发送完成关闭
"""


from socket import *

# 创建套接字
sock = socket()

# 连接服务端
sock.connect(('127.0.0.1',8888))

# 读取图片内容
f = open("sg.jpeg",'rb')

while True:
    data = f.read(1024)  # 字节串1024是1kB，1024*1024是1MB
    if not data:         # 到文件结尾结束循环
        break
    sock.send(data)     # 一边读取，一边发送图片内容

# 关闭
f.close()
sock.close()
