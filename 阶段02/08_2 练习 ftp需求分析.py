
'''
ftp功能
需求分析：
    【1】 分为服务端和客户端，要求可以有多个客户端同时操作。
    【2】 客户端可以查看服务器文件库中有什么文件。
    【3】 客户端可以从文件库中下载文件到本地。
    【4】 客户端可以上传一个本地文件到文件库。
    【5】 使用print在客户端打印命令输入提示，引导操作

技术点分析 ： C / S
    * 并发模型　：　多线程
    * 网络：　ＴＣＰ网络
    * 文件传输　：　　边读边发　　　边收边写

功能模块划分和封装　：　 函数＋类,即整体框架写在函数main（）里，具体功能写在类里
　　　* 搭建整体结构框架
　　　* 查看文件目录
     * 下载文件
     * 上传文件

通信协议：
    　　　　　　　　　　　　请求类型　　　　数据参量
    　获取文件列表　　　　　　LIST
      下载文件　　　　　　　　RETR　　　　　filename
      上传文件     　　　　　STOR　　     filename
      退出　　　　　　　　　　EXIT

具体功能逻辑
    　* 搭建整体结构框架
         服务端 ： tcp多线程并发模型

　　　* 查看文件目录
         客户端 ： 输入指令 list
                  发送请求
                  等待回复，根据回复请求做下一步处理
                          客户端发送请求
                            ---》服务端根据客户端的请求，可能有不同的情况，
                                 例如：ftp服务器目录为空，回复什么给客户端，不为空，回复什么给客户端
                                      要下载的文件存在，回复什么，不存在，回复什么
                                      要上传的文件，上传过了，回复什么，没上传过，回复什么
                                     【【【!!!!!!!!!!这个请求应答模型比较重要,再加上run函数里的总分、客户端给服务端发消息的通信协议，三个部分很重要】】】
                  OK : 接收文件列表
                  FAIL : 结束

         服务端 ： 接收请求
                  判断请求是否可以满足
                  给出回复
                  OK ： 发送文件列表
                  FAIL : 结束

     * 下载文件
          客户端 ：　发送请求
          　　　　　　等待反馈
          　　　　　　OK  接收文件
          　　　　　　FAIL　结束

          服务端 ： 接收请求
                   判断文件是否存在，给出结果
                   ok 发送文件
                   FAIL 结束

     * 上传文件
          客户端 ：　发送请求
          　　　　　　等待反馈
          　　　　　　OK  上传文件
          　　　　　　FAIL　结束

          服务端 ： 接收请求
                   判断文件是否存在，给出结果
                   ok 接受文件
                   FAIL 结束

'''
