"""

从客户端可以循环的输入单词
服务端查询到单词，将单词的解释发送给客户端，让客户端打印

单词通过数据表words查询

思路： 客户端输入一个单词，发送一次，然后等接收，打印
     服务端，接收单词，查询单词 将解释发送给客户端

"""


'''

服务端要先执行，
因为客户端，是要访问服务端的ip、端口的，
所以服务端要先跑起来

'''


from socket import *
import pymysql



# 创建数据库类，
class Database:
    def __init__(self):       # 构造函数里就连接数据库、创建游标，则创建数据库类的对象时，就会连接数据库、创建游标
        self.db = pymysql.connect(user="work",
                                  password="123",
                                  database="dict",
                                  charset="utf8")
        self.cur = self.db.cursor()

    def close(self):             #关闭游标、关闭数据库连接
        self.cur.close()
        self.db.close()

    def find_word(self,word):   #查询操作
        """
        :param word: 要查询的单词
        :return:     返回查询得到的解释
        """
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql,[word])
        result = self.cur.fetchone()
        if result:
            return result[0] # 返回解释
        else:
            return "Not Found"


# 确定服务器地址,全局变量
ADDR = ('0.0.0.0', 8888)



def main():
    # 创建udp套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    # 绑定地址
    udp_socket.bind(ADDR)

    db = Database() # 生成数据库对象

    while True:
        # 等待接受客户端发来的单词，接收单词
        # 发送跟接受，要成对匹配出现，否则只有接受，没有发送，则会一直等待
        word, addr = udp_socket.recvfrom(1024)
        # 查询单词
        result = db.find_word(word.decode())

        udp_socket.sendto(result.encode(), addr)  # 给对应客户端发送消息

    db.close()
    udp_socket.close()


if __name__ == '__main__':
    main() # 启动







