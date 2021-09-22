
'''

### 4.1 HTTP协议
* 用途 ： 网页获取，数据的传输
* 特点
  * 应用层协议，使用tcp进行数据传输
  * 简单，灵活，很多语言都有HTTP专门接口
  * 无状态，数据传输过程中不记录传输内容
  * 有丰富了请求类型
  * 可以传输的数据类型众多



#### 4.1.2 网页访问流程
1. 客户端（浏览器）通过tcp传输，发送http请求给服务端
   服务端接收到http请求后进行解析
   服务端处理请求内容，组织响应内容
2、服务端将响应内容以http响应格式发送给浏览器
   浏览器接收到响应内容，解析展示

'''




'''

#### 4.1.2 HTTP请求【四部分】
1、
- 请求行【只占一行】 ： 具体的请求类别和请求内容
        GET         /        HTTP/1.1
        请求类别   请求内容的路径     协议版本

        请求类别：每个请求类别表示要做不同的事情
            GET : 获取网络资源
            POST ：提交一定的信息，得到反馈
            HEAD ： 只获取网络资源的响应头
            PUT ： 更新服务器资源【例如网盘上传】
            DELETE ： 删除服务器资源【例如网盘删除】
2、
- 请求头：对请求的进一步解释和描述【键值对的形式】
        例如压缩方式gzip
        Accept-Encoding: gzip
3、
- 空行
4、
- 请求体: 请求参数或者提交内容


'''




'''
#### 4.1.3 HTTP响应【四部分】
1、
- 响应行【只占一行】 ： 反馈基本的响应情况
        HTTP/1.1     200       OK
        版本信息       响应码   附加信息

        响应码 ：
        1xx  提示信息，表示请求被接收
        2xx  响应成功
        3xx  响应需要进一步操作，重定向
        4xx  客户端错误
        5xx  服务器错误
2、
- 响应头：对响应内容的描述【键值对】
        Content-Type: text/html     【响应的内容是网页】
        Content-Length:109\r\n      【响应的内容是109字节】
3、
- 空行
4、
- 响应体：响应的主体内容信息



'''

"""
http 请求响应演示
"""

# from  socket import *
#
# # 创建tcp套接字
# s = socket()
# s.bind(("0.0.0.0",8888))
# s.listen(5)
#
# c,addr = s.accept()
# print("Connect from",addr)
# data = c.recv(4096)
# print(data.decode())    # 浏览器访问http://127.0.0.1:8888或者http://127.0.0.1:8888/wangfei等，随便访问，打印出收到的http请求
#
# # 不管请求什么内容，都如下回复给浏览器
# # 要把发送给浏览器的内容，按照http响应格式，写出来，
# # 四部分，响应行、响应头、空行、响应体都有，格式不能错了，否则浏览器解析不了，打印不出响应体的内容
# # 响应内容一般是前端工程师写，跟后端代码是分开的
# html = """HTTP/1.1 404 Not Found
# Content-Type:text/html
#
# Sorry....
# """
#
# c.send(html.encode())   # 发送响应给客户端，即发给浏览器
#
# c.close()
# s.close()



'''
收到的请求如下，只有请求行【即第一行】、请求头【剩下所有】，空行【最后一行】
GET /wangfei HTTP/1.1
Host: 127.0.0.1:8888
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1


'''






"""
练习1： 
浏览器可以多次【循环】访问index.html这个页面
服务端把这个网页内容http响应回复给浏览器，显示在浏览器上

如下，浏览器访问http://127.0.0.1:8888或者http://127.0.0.1:8888/wangfei等，随便访问，就可以显示index.html这个页面了

但是这个是循环模型，
跟一个浏览器请求、响应完成后，
才能跟另一个浏览器建立tcp 三次握手 accept,然后请求响应
"""
#
# from  socket import *
#
# # 创建tcp套接字
# s = socket()
# s.bind(("0.0.0.0",8888))
# s.listen(5)
#
# while True:
#     c,addr = s.accept()
#     print("Connect from",addr)
#     data = c.recv(4096)                 # 接收的是http请求
#     print(data.decode().split('\n')[0]) # 打印请求行
#
#     # http响应格式
#     f = open("index.html")
#     html = "HTTP/1.1 200 OK\r\n"        #【\r\n表示换行】
#     html += "Content-Type:text/html\r\n"
#     html += "\r\n"
#     html += f.read()                # 响应体【默认以只读模式打开文本，不加参数表示读取文件所有内容】
#     c.send(html.encode())           # 发送响应给客户端
#     f.close()
#     c.close()
#
# s.close()



'''
练习:   IO 多路复用和 http训练
即当前目录下，有个前端工程师写的网站，即目录static,里面有好多个网页

web服务的程序实现，即实现如下功能
1. 主要功能 ：
     【1】 接收客户端（浏览器）请求
     【2】 解析客户端发送的请求
     【3】 根据请求组织数据内容
     【4】 将数据内容形成http响应格式返回给浏览器

2. 特点 ：【即框架】
     【1】 采用IO并发，可以满足多个客户端同时发起请求情况
     【2】 通过类接口形式进行功能封装
     【3】 做基本的请求解析，根据具体请求返回具体内容，同时处理客户端的非网页请求行为
     

使用类进行封装：
假定 ： 用户有一组网页，希望使用我们提供的类，快速搭建一个服务，实现自己网页的展示浏览

如何对功能进行类封装设计：
1. 从功能使用方法的角度分析,【即使用者，是怎么用的】

2. 借鉴自己曾经用过的Python类，例如下面
    socket()
       实例化对象 ————> 用户可以选择何种套接字对象【比如tcp，udp套接字对象，不同的套接字对象功能不同，即不同对象能够调用的方法不一样】

    Process()
       实例化对象 ----> 功能单一
       固定的流程去实现指定功能 ： Process()  start()  join()
       用户决定：使用进程干什么

3. 设计原则
   * 站在用户角度，想用法
   * 能够为用户实现的 不麻烦使用者
   * 不能提使用者决定的，提供接口（参数） 让用户方便传递或者让用户调用不同的方法做选择

4. 编写步骤  ： 先搭建框架，再实现具体业务逻辑

'''

from socket import *
from select import select
import re


class WebServer:
    def __init__(self, host='0.0.0.0', port=80, html=None):
        self.host = host
        self.port = port
        self.html = html
        # 做IO多路复用并发模型准备
        self.__rlist = []      #【属性不一定非要传参传进来，也可以直接写，这里写成了私有属性】
        self.__wlist = []
        self.__xlist = []
        self.create_socket()    #【init函数里也可以执行一些函数用于初始化】
        self.bind()

    # 创建套接字
    def create_socket(self):   #self.sock ，self.address，这些属性不一定写在init函数里，别的函数里也可以写属性
        self.sock = socket()
        self.sock.setblocking(False)

    def bind(self):
        self.address = (self.host, self.port)
        self.sock.bind(self.address)

    # 启动服务
    def start(self):
        self.sock.listen(5)
        print("Listen the port %d" % self.port)
        # IO多路复用并发模型
        self.__rlist.append(self.sock)
        while True:
            # 循环监听IO
            rs, ws, xs = select(self.__rlist, self.__wlist, self.__xlist)
            for r in rs:
                if r is self.sock:
                    # 有浏览器连接
                    connfd, addr = self.sock.accept()
                    connfd.setblocking(False)
                    self.__rlist.append(connfd)
                else:
                    # 浏览器发送请求，如果请求的时候加一些特殊字符，则没办法被decode，request = connfd.recv(1024 * 10).decode()
                    try:
                        self.handle(r)
                    except:
                        self.__rlist.remove(r)
                        r.close()

    # 处理客户端请求
    def handle(self, connfd):
        # 浏览器发送了HTTP请求
        request = connfd.recv(1024 * 10).decode()
        # print(request)
        # 使用正则提取请求内容
        pattern = "[A-Z]+\s+(?P<info>/\S*)"
        result = re.match(pattern, request)  # 返回match对象 ，如果没有匹配到，则返回None
        if result:
            info = result.group('info')  # 提取请求内容
            print("请求内容:", info)
            # 发送响应内容
            self.send_response(connfd, info)
        else:
            # 没有获取请求断开客户端
            self.__rlist.remove(connfd)
            connfd.close()

    # 根据请求组织响应内容，发送给浏览器
    def send_response(self, connfd, info):
        if info == '/':
            # 主页
            filename = self.html + "/index.html"
        else:
            filename = self.html + info

        try:
            fd = open(filename,'rb') # 有可能有文本，还有图片，所以用二进制只读打开
        except:
            # 请求的文件不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += "<h1>Sorry....</h1>"
            response = response.encode()
        else:
            # 请求的文件存在
            data = fd.read()
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "Content-Length:%d\r\n"%len(data) # 发送图片的大小
            response += "\r\n"
            response =response.encode() + data # 转换成字节串后，再拼接
        finally:
            # 给客户端发送响应
            connfd.send(response)


if __name__ == '__main__':
    """
    思考问题 :   1. 使用流程
               2. 那些量需要用户决定，怎么传入
              例如，1、服务要给浏览器响应哪组网页？
                   2、服务部署在哪台机器上，即服务端地址、端口？

    """
    # 实例化对象
    httpd = WebServer(host='0.0.0.0', port=8000, html="./static")
    # 启动服务
    httpd.start()
