''
'''
通信协议设计：
            这个思想很重要，对应的是server的while  if总分结构

通信协议设计 ： 数据传输中双方做一些数据格式和含义的约定，客户端和服务端同时遵守就行，
              请求类型和数据参量【即传给服务端的数据】都是程序员自己定义的
              将请求类型和数据参量一起发给服务端，服务端判断客户端想要做什么

                请求类型              数据参量
   登录聊天室      L【login】           name
　　
　　聊天　　　　　　 C【chart】           name 消息内容

   退出           E 【exit】           name




需求分析 ： 要点 -》构建出软件的基本使用方法
    【1】 有人进入聊天室需要输入姓名，姓名不能重复
    【2】 有人进入聊天室时，其他人会收到通知：xxx 进入了聊天室
    【3】 一个人发消息，其他人会收到：xxx ： xxxxxxxxxxx
    【4】 有人退出聊天室，则其他人也会收到通知:xxx退出了聊天室


技术分析 ： 使用的技术
    * C / S 模型
    * 服务端存储用户信息 ： 姓名 和 address,可以用列表、字典、类
      [(name,address),....]
      {name:address}
      class Person:
        def __init__(self,name,address):
            self.name = name
            self.address = address
    * 网络通信 ： udp
    * 服务端消息传输机制:  客户端 ---》 服务端 --》转发给其他客户端
    * 客户端收发消息互不影响 ： 多进程，一个进程负责收消息，一个负责发消息


功能模块分析
    * 整体框架设计
    * 登录聊天室
    * 聊天
    * 退出聊天室
    封装 ： 函数


模块逻辑设计
    * 整体框架设计
    【以服务端为出发点，去思考】
          服务端： 1.创建udp网络套接字
                  2.循环接收来自客户端的请求
                  3.根据请求调用不同的函数去解决
    
          客户端： 1. 建立网络套接字

    *不同请求如下：
    【不同的请求，或不同的功能，以客户端为出发点去思考，因为客户端是功能的发出者，服务端只是满足功能】
    
        * 进入聊天室
           客户端 ： 1.输入用户名
                    2. 发送用户名
                    3. 等待进入聊天室 --》 Y 进入聊天室聊天
                                        N  重新输入
           服务端:  1. 接收用户名
                   2. 判断是否已经存在
                   3. 存在 --》 告知客户端 无法进入
                      不存在 --》 告知客户端进入聊天室
                   4. 客户端进入聊天室则  存储用户信息，告知其他用户
    
        * 聊天
             客户端 ：　创建子进程
             　　　　　　父进程循环发送消息
             　　　　　　子进程循环接收消息【因为子进程不能使用input】
           　 服务端　：　接收消息
           　　　　　　　　转发给其他人
    
        * 退出聊天室

优化完善
* 显示效果
* 客户端强行退出


'''