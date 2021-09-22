'''
### 3.3 IO并发模型

*什么是IO
【即数据在内存中的输入输出】
在程序中存在读、写数据操作行为的事件，均是IO行为，
比如终端输入input、输出print, 文件读写，数据库修改和网络消息收发等。


*程序分类
*IO密集型程序：在程序执行中有大量IO操作，而运算操作较少。
            消耗cpu较少，耗时比较长。
*计算密集型程序：程序运行中运算较多，IO操作相对较少。
            cpu消耗多，执行速度快，几乎没有阻塞。



*IO模型分类：
    阻塞IO
    非阻塞IO
    IO多路复用
    异步IO，等




#### 3.2.2 阻塞IO
*定义：在执行IO操作时如果执行条件不满足则阻塞。
        阻塞IO是IO的默认形态。

*效率：阻塞IO效率很低。
        但是由于逻辑简单所以是默认IO行为。

*阻塞情况
第一种：
*因为某种执行条件没有满足造成的函数阻塞
    例如
    tcp三次握手accept   、input  、 等待接受消息recv

第二种：
*处理IO的时间较长产生的阻塞状态
    例如
    网络传输【比如传输的文件比较大】，
    大文件读写


'''







'''
#### 3.2.3 非阻塞IO
*定义 ：通过修改IO属性行为，使原本阻塞的IO变为非阻塞的状态。
    【即不会阻塞等待，而是继续执行代码，处理别的任务，前提是别的任务，不能依赖当前的还没执行的任务】

例如
第一种：
- 设置套接字对象为非阻塞IO
sockfd.setblocking(False)
功能：设置套接字为非阻塞IO
参数：默认为True，表示套接字IO阻塞；
    设置为False则套接字IO变为非阻塞

第二种：
- 超时检测 ：给套接字对象，设置一个最长阻塞时间，超过该时间后则不再阻塞等待。
sockfd.settimeout(sec)
功能：设置套接字的超时时间
参数：设置的时间

'''

"""
非阻塞IO举例：
    把套接字对象，由原本的阻塞，变成非阻塞
    
第一种：
sockfd.setblocking(False)
参数：默认为True，表示套接字IO阻塞；
    设置为False则套接字IO变为非阻塞
"""
# from socket import *
# import time
#
# # 打开日志文件【追加模式】
# f = open("my.log",'a')
#
# # 创建tcp套接字
# sockfd = socket()
# sockfd.bind(('0.0.0.0',8888))
# sockfd.listen(5)
#
# # 设置套接字为非阻塞，则sockfd对象调用的所有函数，都变成非阻塞
# sockfd.setblocking(False)
#
#
# while True:
#     print("Waiting for connect")
#     try:
#         connfd,addr = sockfd.accept() # 如果没有客户端跟服务器建立tcp三次握手，则执行except的代码，即做点别的事，这里是每隔两秒记录日志到文件里
#         print("Connect from",addr)
#     except BlockingIOError as e:
#         # 干点别的事
#         msg = "%s : %s\n"%(time.ctime(),e)
#         f.write(msg)
#         time.sleep(2)
#     else:                               # 如果有客户端三次握手accept连接，则执行如下，recv还是会阻塞，
#                                         # 因为设置非阻塞的是sockfd，而不是connfd，也可以给connfd设置非阻塞
#         data = connfd.recv(1024)
#         print(data.decode())
#
#


'''
非阻塞IO举例：

第二种：
- 超时检测 ：给套接字对象，设置一个最长阻塞时间，超过该时间后则不再阻塞等待。
sockfd.settimeout(sec)

'''
#
# from socket import *
# import time
#
# # 打开日志文件【追加模式】
# f = open("my.log",'a')
#
# # 创建tcp套接字
# sockfd = socket()
# sockfd.bind(('0.0.0.0',8888))
# sockfd.listen(5)
#
#
# # 超时检测时间
# sockfd.settimeout(3)
#
# while True:
#     print("Waiting for connect")
#     try:
#         connfd,addr = sockfd.accept() # 如果等3s后，没有客户端跟服务器建立tcp三次握手，则执行except的代码，即做点别的事，
#                                       #这里是记录日志到文件里,因为超时时间设置成3s了
#         print("Connect from",addr)
#     except timeout as e:
#         # 干点别的事
#         msg = "%s : %s\n"%(time.ctime(),e)
#         f.write(msg)
#     else:                               # 如果有客户端三次握手accept连接，则执行如下，recv还是会阻塞，因为设置非阻塞的是sockfd，而不是connfd
#         data = connfd.recv(1024)
#         print(data.decode())











'''

#### 3.2.4 IO多路复用【一般用于网络套接字编程】

操作系统同时监控多个IO事件  【监控的是IO对象，而不是IO对象的行为，例如文件对象f=open（）、数据库对象、套接字对象】，
当哪些IO事件准备就绪       【即不用继续阻塞等待了，例如有客户端来建立三次握手accept了；或者input输入内容后，按回车； 】，
操作系统就让应用层执行哪些IO事件。
以此形成可以同时处理多个IO的行为，
避免一个IO阻塞，造成其他IO均无法执行，提高了IO执行效率。




*具体方案【三种方法功能都是一样的，实现IO多路复用】
第一种：【用的比较多】
*select方法 ： windows、linux、unix

第二种：
*poll方法： linux、unix

第三种：【用的比较多】
*epoll方法： linux




*select方法

rs, ws, xs = select(rlist, wlist, xlist[, timeout])

功能: 监控多个IO事件【文件、数据库、套接字对象】，
     阻塞、等待IO发生【等待就绪】

参数：
     rlist   列表  读IO列表，添加等待发生的或者可读的IO事件     
     【文件read,数据库select,udp套接字和tcp连接套接字的recv、tcp套接字accept、tcp套接字listen，这些都是被动等待的，这个读IO列表用的比较多】

     wlist   列表  写IO列表，存放要可以主动处理的或者可写的IO事件
     【文件read、write，udp套接字和tcp连接套接字的send、tcp套接字connect，这些都是主动发生，不需要等待的，即这些都是就绪的】
     
     xlist   列表  异常IO列表，存放出现异常要处理的IO事件       
     【基本不用】
     
     timeout 超时时间                                     
     【不写就是死等，写就是最多等多久】

返回值： 【如果select在死等，只要有一个io就绪，就有返回值，即表示返回的三个列表，至少有一个列表不是空，否则select应该在等待】
        rs  列表  rlist中准备就绪的IO对象
        ws  列表  wlist中准备就绪的IO对象
        xs  列表  xlist中准备就绪的IO对象
        

        
'''

"""
select io 多路复用
"""

# from socket import *
# from select import select
# from time import sleep
#
#
# # 创建三个对象，帮助监控
#
# #tcp套接字对象，有客户端连接来accept建立三次握手，则就绪
# tcp_sock = socket()
# tcp_sock.bind(('0.0.0.0',8888))
# tcp_sock.listen(5)
# print(tcp_sock)
#
# #udp套接字对象，有客户端发消息过来，则就绪
# udp_sock = socket(AF_INET,SOCK_DGRAM)
# udp_sock.bind(('0.0.0.0',8866))
#
# #文件对象
# f = open("my.log",'rb')
#
#
# # 开始监控这些IO对象
# print("监控IO发生")
# sleep(5)
# rs,ws,xs = select([tcp_sock],[f,udp_sock],[],3)   #这里把tcp套接字放到可读列表监控，文件对象和udp套接字，放到可写列表监控
# print("rs :",rs)
# print("ws :",ws)
# print("xs :",xs)
#
#
# 如果此时有tcp客户端连接，则返回值列表如下：
# tcp套接字就绪了，因为在可读io列表里，有客户端连了，
# 文件套对象、跟udp套接字，在可写io列表里，本来就是就绪的
# rs : [<socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 8888)>]
# ws : [<_io.BufferedReader name='my.log'>, <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_DGRAM, proto=0, laddr=('0.0.0.0', 8866)>]
# xs : []







'''

#### 3.2.5 IO并发模型       【使用的就是单进程，这里不考虑多进程、多线程，因为多进程多线程本来就可以处理多个客户端的请求,而不仅仅是io请求】

利用IO多路复用等技术，同时处理多个客户端IO请求。
*优点 ： 资源消耗少【因为不用创建多进程或多线程】，能同时高效处理多个IO行为
*缺点 ： 只处理并发产生的IO事件
*适用情况：HTTP请求，网络传输等都是IO行为，可以通过IO多路复用监控多个客户端的IO请求。



*并发服务实现过程
【1】将关注的IO准备好，通常设置为非阻塞状态。
【2】通过IO多路复用方法提交，进行IO监控。
【3】阻塞等待，当监控的IO有发生时，结束阻塞。
【4】遍历返回值列表，确定就绪IO事件。
【5】处理发生的IO事件。
【6】继续循环监控IO发生。

'''

"""
基于select 的IO多路复用并发模型【tcp】
重点代码 ！
"""
# from socket import *
# from select import select
#
# # 全局变量
# HOST = "0.0.0.0"
# PORT = 8888
# ADDR = (HOST, PORT)
#
# # 创建tcp套接字
# tcp_socket = socket()
# tcp_socket.bind(ADDR)
# tcp_socket.listen(5)
#
# # 设置为非阻塞
# tcp_socket.setblocking(False)
#
# # IO对象监控列表
# rlist = [tcp_socket]  # 监听tcp监听套接字的可读IO
# wlist = []
# xlist = []
#
# # 循环监听
# while True:
#     # 初始状态是对tcp监听套接字进行监控，
#
#     # ！！初始状态下，select语句只要有返回值，表示IO就绪，即有客户端连接进来，则不再阻塞等待，
#     # 而是执行下面代码，将客户端的连接套接字connfd添加到列表rlist，来一个客户端，就添加一次
#
#     # 当已经创建多个连接套接字后，select语句的返回值列表rlist的元素也会很多，比如有tcp监听套接字【有新客户端连进来了】和客户端连接套接字【客户端发消息来了】
#
#     # ！！多个客户端发消息过来时，则多个连接套接字connfd就绪，执行下面的收发消息代码
#     # 这段代码的执行速度一定要快，不能阻塞，否则没办法执行下一轮循环，即没办法select监控哪些IO又就绪了，
#     # 所以一般把套接字、连接套接字全部设置成非阻塞，防止任何地方阻塞等待
#     rs, ws, xs = select(rlist, wlist, xlist)
#
#     # 对返回值可读列表rs，分情况讨论列表里的元素，包括监听套接字、客户端连接套接字
#     for r in rs:
#         if r is tcp_socket:             # 处理客户端连接，即有客户端建立tcp三次握手，则创建的tcp套接字就绪【对象相等用is】
#             connfd, addr = r.accept()
#             print("Connect from", addr)
#             connfd.setblocking(False)   # 设置连接套接字非阻塞
#             rlist.append(connfd)        # 添加到监控列表
#         else:
#             data = r.recv(1024)         # 收消息，有客户端发消息来
#             if not data:
#                 rlist.remove(r)         # 客户端退出，连接套接字也会就绪，recv返回空，则监听列表移除这个连接套接字、关闭连接套接字、进入下一轮for循环处理别的连接套接字
#                 r.close()
#                 continue
#             print(data.decode())
#             #r.send(b'OK')
#             wlist.append(r)             # 这里可以直接r.send(b'OK')，而且一般都是直接写
#                                         # 如果不直接写，也可以把连接套接字放入可写列表wlist进行select监听，
#                                         # 然后这个for循环执行完后，进入下一轮while循环，select返回值ws里有这个连接套接字，则执行下面的for循环
#
#     for w in ws:
#         w.send(b"OK")                   # 发送消息
#         wlist.remove(w)                 # 如果不移除，每执行一次while循环，会发一次ok给这个客户端
#









'''
io多路复用

第二种方法： *poll方法

p = select.poll()
功能 ： 创建poll对象
返回值： poll对象


p.register(fd, event)
功能: 注册关注的IO事件【文件、数据库、套接字对象】
参数：fd      要关注的IO【套接字对象】
     event   要关注的IO事件类型
        常用类型：POLLIN   读IO事件（类似select的rlist）
                POLLOUT  写IO事件 (类似wlist)
                POLLERR  异常IO  （类似xlist）
                POLLHUP  断开连接
        例如 p.register(sockfd, POLLIN | POLLERR)，关注套接字对象的POLLIN 和 POLLERR事件



p.unregister(fd)
功能：取消对IO对象的关注【文件、数据库、套接字对象】
参数：IO对象或者IO对象的fileno


events = p.poll()
功能：   阻塞等待监控的IO事件发生【等待对象就绪】
返回值： 返回发生的IO事件列表
        【返回列表，列表的一个元素就是就绪的对象，元素是一个元组】
        元组第一项是该IO的fileno文件描述符，第二项为该IO就绪的事件类型
        events格式[(fileno, event), ()....]
        

        文件描述符 ： 每个IO【文件、数据库、套接字对象】在系统中都有一个系统分配的 >= 0的整数编号，即文件描述符
        特点:       不会重复, 每个文件描述符对应一个IO对象
        查看 ：      IO对象.fileno()
        
        由于返回值是就绪的对象的文件描述符，所以需要用字典，通过文件描述符作为键，确定对应的对象
'''

"""
poll io 多路复用
"""

# from socket import *
# from select import *
# from time import sleep
#
# # 创建三个对象，帮助监控
# tcp_sock = socket()
# tcp_sock.bind(('0.0.0.0',8888))
# tcp_sock.listen(5)
#
# udp_sock = socket(AF_INET,SOCK_DGRAM)
# udp_sock.bind(('0.0.0.0',8866))
#
# f = open("my.log",'rb')
#
# # 创建poll对象
# print("监控IO发生")
# p = poll()
#
# # 关注需要被监控的对象、以及可读还是可写等的事件类型
# p.register(tcp_sock,POLLIN)
# p.register(f,POLLOUT)
# p.register(udp_sock,POLLOUT|POLLIN)
#
# #打印被监控的对象的文件描述符
# print("tcp_sock:",tcp_sock.fileno())
# print("udp_sock:",udp_sock.fileno())
# print("file:",f.fileno())
#               # tcp_sock: 3
#               # udp_sock: 4
#               # file: 5
#
# # 字典，通过文件描述符，确定被监控的对象
# map = {
#        tcp_sock.fileno():tcp_sock,
#        udp_sock.fileno():udp_sock,
#        f.fileno():f
#        }
#
# events = p.poll() # 进行监控，返回就绪的对象
# print(events)  # 返回值：[(5, 4), (4, 4)]
                        # 第一个元组表示文件描述符5即文件对象，事件类型4即POLLOUT可写事件，就绪
                        # 第二个元组表示文件描述符4即udp套接字对象，事件类型4即POLLOUT可写事件，就绪
#
# p.unregister(f) # 取消关注




"""
练习：

基于poll方法实现IO多路复用并发【tcp】
"""
#
# from socket import *
# from select import *
#
# # 全局变量
# HOST = "0.0.0.0"
# PORT = 8888
# ADDR = (HOST,PORT)
#
# # 创建tcp套接字
# tcp_socket = socket()
# tcp_socket.bind(ADDR)
# tcp_socket.listen(5)
#
# # 设置为非阻塞
# tcp_socket.setblocking(False)
#
# p = poll()                    # 建立poll对象
# p.register(tcp_socket,POLLIN) # 监控套接字对象的可读事件
#
# # 准备工作，建立文件描述符 和 IO对象对应关系的字典
# # 字典应该时刻与register关注的对象【文件、数据库、套接字对象】一致
# # 用于通过文件描述符，确定被监控的对象
# map = {tcp_socket.fileno():tcp_socket}
#
# # 循环监听被关注的对象【文件、数据库、套接字对象】
# while True:
#     # 对关注的IO对象进行监控，返回列表，列表的元素是元组，元组包含就绪的对象文件描述符和对应的事件类型【可读 可写等】
#     #events--> [(fileno,event),()....]
#     events = p.poll()
#
#     for fd,event in events:
#         if fd == tcp_socket.fileno():          # 如果文件描述符等于监听套接字的文件描述符，则有客户端连接进来，进行accept tcp三次握手
#             connfd, addr = map[fd].accept()    # 通过文件描述符这个键，找套接字对象这个值
#             print("Connect from", addr)
#             connfd.setblocking(False)          # 设置非阻塞
#             p.register(connfd,POLLIN|POLLERR)  # 连接套接字添加到监控
#             map[connfd.fileno()] = connfd      # 把连接套接字的文件描述符和连接套接字，作为键和值，添加到字典
#         elif event == POLLIN:
#             # 收消息,当连接套接字关注多个事件，可以这样写判断event == POLLIN，或者event & POLLIN，只在收消息的时候，执行下面代码
#             data = map[fd].recv(1024)
#             if not data:
#                 # 客户端退出
#                 p.unregister(fd) # 移除关注连接套接字connfd
#                 map[fd].close()  # 关闭connfd
#                 del map[fd]      # 从字典也移除connfd
#                 continue
#             print(data.decode())
#             map[fd].send(b'OK')
#











'''
*epoll方法

使用方法 ：基本与poll相同，除了下面两点，别的都一样
1、生成对象改为epoll()
2、将所有事件类型改为EPOLL类型



*epoll特点
*epoll效率比select 、poll要高
*epoll监控IO数量比select要多
*epoll的触发方式【事件类型】比poll要多 （EPOLLET边缘触发）

'''

"""
基于epoll方法实现IO并发【tcp】

重点代码 !
原理分析参照上面的poll方法举例

"""
#
# from socket import *
# from select import *
#
# # 全局变量
# HOST = "0.0.0.0"
# PORT = 8888
# ADDR = (HOST, PORT)
#
# # 创建tcp套接字
# tcp_socket = socket()
# tcp_socket.bind(ADDR)
# tcp_socket.listen(5)
#
# # 设置为非阻塞
# tcp_socket.setblocking(False)
#
# p = epoll()  # 建立epoll对象
# p.register(tcp_socket, EPOLLIN)  # 初始监听对象
#
# # 准备工作，建立文件描述符 和 IO对象对应的字典  时刻与register的IO一致
# map = {tcp_socket.fileno(): tcp_socket}
#
# # 循环监听
# while True:
#     # 对关注的IO进行监控
#     events = p.poll()
#     # events--> [(fileno,event),()....]
#     for fd, event in events:
#         # 分情况讨论
#         if fd == tcp_socket.fileno():
#             # 处理客户端连接
#             connfd, addr = map[fd].accept()
#             print("Connect from", addr)
#             connfd.setblocking(False)  # 设置非阻塞
#             p.register(connfd, EPOLLIN | EPOLLERR)  # 添加到监控
#             map[connfd.fileno()] = connfd  # 同时维护字典
#         elif event == EPOLLIN:
#             # 收消息
#             data = map[fd].recv(1024)
#             if not data:
#                 # 客户端退出
#                 p.unregister(fd)  # 移除关注
#                 map[fd].close()
#                 del map[fd]  # 从字典也移除
#                 continue
#             print(data.decode())
#             map[fd].send(b'OK')









'''

io多路复用方法对比                      

                平台支持                    监控IO数量     执行效率
select         优秀（windows、linux、unix）   1024         一般

poll           良好（Linux，unix）           无限制         一般

epoll          较差（Linux）                 无限制         较高

监控IO数量： 例如套接字+连接套接字的总数量，即能有多少客户端连到服务器


'''
