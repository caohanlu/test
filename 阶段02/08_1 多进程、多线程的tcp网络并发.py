
'''
## 3. 网络并发模型
* 什么是网络并发
  在实际工作中，一个服务端程序往往要应对多个客户端同时发起访问的情况。
  如果让服务端程序能够同时满足更多客户端网络请求的情形，这就是并发网络模型。

* 循环网络模型问题
  循环网络模型只能循环接收客户端请求，处理请求。
  同一时刻只能处理一个客户端请求，处理完毕后再处理下一个客户端。
  这样的网络模型虽然简单，资源占用不多，但是无法同时处理多个客户端请求就是其最大的弊端，往往只有在一些低频的小请求任务中才会使用。


'''




'''
### 3.2 多任务网络并发模型

多任务并发模型具体指,多进程、多线程网络并发模型，
即每当一个客户端连接服务器，就创建一个新的进程或线程，为该客户端服务；
客户端退出时，再销毁该进程或线程，

多任务并发模型也是实际工作中最为常用的服务端处理模型。
    * 优点：能同时满足多个客户端长期占有服务端需求，可以处理各种请求。
    * 缺点： 资源消耗较大
    * 适用情况：客户端请求较复杂，需要长时间占有服务器。
    
'''



'''

#### 3.1.1 多进程网络并发模型【tcp】

* 创建网络套接字用于接收客户端请求
* 等待客户端连接
* 客户端连接，则创建新的进程具体处理客户端请求
* 主进程继续等待其他客户端连接
* 如果客户端退出，则销毁对应的进程


'''

"""
基于多进程的 tcp 网络并发模型【server端】
重点代码！！
"""
# from socket import *
# from multiprocessing import Process
# from signal import *
#
# # 全局变量
# HOST = '0.0.0.0'
# PORT = 8888
# ADDR =  (HOST,PORT) #  服务器地址
#
# # 处理客户端请求，这里以跟客户端循环收发消息为例子
# def handle(connfd):
#     while True:
#         data = connfd.recv(1024)
#         # 另外一端不存在了，recv会返回空字节
#         if not data:
#             break
#         print("Recv:",data.decode())
#         connfd.send(b"Thanks")
#     connfd.close()
#
# def main():
#     sock = socket()
#     sock.bind(ADDR)
#     sock.listen(5)
#     print("Listen the port %s"%PORT)
#     signal(SIGCHLD,SIG_IGN)          # 子进程执行完毕，父进程由于是循环，正常情况下是不会退出的，所以造成僵尸进程，让操作系统处理僵尸进程
#
#     # 循环、等待客户端，accept建立tcp三次握手
#     while True:
#         try:
#             connfd,addr = sock.accept()
#             print("Connect from",addr)
#         except KeyboardInterrupt:
#             sock.close()
#             return
#         # 为连接进来的客户端创建单独的子进程,把这个客户端的连接套接字connfd传给函数，来跟这个特定的客户端收发消息
#         p = Process(target = handle,args=(connfd,))
#         p.daemon = True # 父进程退出，子进程终止服务；并且start后面不能join，否则父进程就阻塞等待，没办法循环跟别的客户端建立tcp三次握手
#         p.start()
#
# if __name__ == '__main__':
#     main()







'''

#### 3.1.2 基于多线程的 tcp 网络并发模型

- 创建网络套接字用于接收客户端请求
- 等待客户端连接
- 客户端连接，则创建新的线程具体处理客户端请求
- 主线程继续等待其他客户端连接
- 如果客户端退出，则销毁对应的线程


线程没有僵尸进程的概念，所以不用处理僵尸进程

'''
#写法跟上面的多线程tcp并发类似

# from socket import *
# from threading import Thread
#
# HOST='127.0.0.1'
# PORT=8888
# ADDR=(HOST,PORT)
#
# def handle(connfd):
#     while True:
#         data=connfd.recv(1024)
#         if not data:
#             break
#         print("Recv:",data.decode())
#         connfd.send(b"Thanks")
#     connfd.close()
#
# def main():
#     sock = socket(AF_INET, SOCK_STREAM)
#     sock.bind(ADDR)
#     sock.listen(5)
#     while True:
#         try:
#             connfd,addr=sock.accept()
#         except KeyboardInterrupt:
#             sock.close()
#             return
#         t=Thread(target=handle,args=(connfd,))
#         t.setDaemon(True)  # 主线程退出，分之线程终止服务
#         t.start()
#
# if __name__ == '__main__':
#     main()






#或
# 也可以使用自定义线程类创建线程

# from socket import *
# from threading import Thread
#
# # 全局变量
# HOST = '0.0.0.0'
# PORT = 8888
# ADDR =  (HOST,PORT) #  服务器地址
#
# # 处理客户端请求
# class MyThread(Thread):
#     def __init__(self,connfd):
#         super().__init__()
#         self.connfd = connfd
#
#     def run(self):
#         while True:
#             data = self.connfd.recv(1024)
#             # 另外一端不存在了，recv会返回空字节
#             if not data:
#                 break
#             print("Recv:",data.decode())
#             self.connfd.send(b"Thanks")
#         self.connfd.close()
#
# def main():
#     # tcp套接字创建
#     sock = socket()
#     sock.bind(ADDR)
#     sock.listen(5)
#     print("Listen the port %s"%PORT)
#
#     # 循环连接客户端
#     while True:
#         try:
#             connfd,addr = sock.accept()
#             print("Connect from",addr)
#         except KeyboardInterrupt:
#             sock.close()
#             return
#         # 为连接进来的客户端创建单独的线程
#         t = MyThread(connfd) # 使用自定义线程类创建线程
#         t.setDaemon(True) # 主线程退出，分之线程终止服务
#         t.start()
#
# if __name__ == '__main__':
#     main()





