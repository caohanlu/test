'''
pymysql模块

使用python，对数据库进行操作

pymysql是一个第三方库，如果自己的计算机上没有可以在终端使用命令进行安装。
sudo pip3 install pymysql

*pymysql使用流程
1.db = pymysql.connect(参数列表)
功能: 链接数据库
host ：主机地址, 本地localhost
port ：端口号, 默认3306
user ：用户名
password ：密码
database ：库名字
charset ：编码方式, 推荐使用utf8

2.
cur = db.cursor()
功能： 创建游标
返回值：返回游标对象, 用于执行具体SQL命令

3.
游标方法:
cur.execute(sql, list_)
功能： 执行SQL命令
参数： sql           ：sql语句
      list_        ：列表，用于给sql语句传递参量


cur.executemany(sql命令, list_)
功能： 多次执行SQL命令，执行次数由列表中元组数量决定
参数： sql         sql语句
      list_       列表中包含元组,每个元组用于给sql语句传递参量，一般用于写操作。

cur.fetchone()
获取查询结果集的第一条数据，查找到返回一个元组，否则返回None

cur.fetchmany(n)
获取前n条查找到的记录，返回结果为元组嵌套元组， ((记录1), (记录2))，查询不到内容返回空元组。

cur.fetchall()
获取所有查找到的记录，返回结果形式同上。





4.
db.commit()
提交到数据库执行

db.rollback()
回滚，用于当commit()出错是回复到原来的数据形态


5.
cur.close()
关闭游标对象

6.
断开数据库连接 ：db.close()



'''





"""

pymysql 操作数据库流程
    跟操作文件类似，打开数据库，操作数据库，关闭数据库
    先把流程复制过来，跑程序，不报错了，再写增删改查，流程如下：
       
# 导入模块
import pymysql

# 连接数据库 (连接自己计算机可以不写host 、port)
# root用户如果登录报错，则创建、授权新的用户，再登录，这里用work用户
db = pymysql.connect(host="localhost",
                     port=3306,
                     user='work',
                     password='123',
                     database='stu',
                     charset='utf8'
                     )

# 创建游标 (游标对象负责调用执行sql语句，操作数据，得到结果)
cur = db.cursor()


# 对数据库操作 （增删改查）


# 关闭游标和数据库
cur.close()
db.close()


"""

# # 导入模块
# import pymysql
#
#
#
# # 连接数据库 (连接自己计算机可以不写host 、port)
# # root用户如果登录报错，则创建、授权新的用户，再登录，这里用work用户
# db = pymysql.connect(host="localhost",
#                      port=3306,
#                      user='work',
#                      password='123',
#                      database='stu',
#                      charset='utf8'
#                      )
#
#
#
# # 创建游标 (游标对象负责调用执行sql语句，操作数据，得到结果)
# cur = db.cursor()
#
#
#
#
# # 对数据库操作 （增删改查）
#
#
#
# #查询操作
#
# # #如下，假设execute执行后，结果里有10条记录，则fetchone()先执行，读取第一行，
# # #                                      fetchmany(2)后执行，读取第二第三两行  ，
# # #                                      fetchall() 最后执行，读取第四到最后一行，有点类似文件的读
# # sql = "select name,age,score from class_1;" # 查询数据库的select语句,以字符串的形式，传给execute
# # cur.execute(sql)                            # 执行sql
# #
# # row = cur.fetchone()                        # 获取一条记录，如果没有结果返回None
# # print(row)                                  #('Lily', 20, 94.0)  是个元组
# #
# #
# # row = cur.fetchmany(2)                     # 获取前两条记录，如果没有结果返回()空元组
# # print(row)                                 #(('Baron', 19, 100.0), ('张三', 10, 91.0))  元组的嵌套
# #
# #
# # row = cur.fetchall()                         # 所有结果，如果没有结果返回()空元组
# # print(row)                                   #(('李四', 9, 90.0), ('张无忌', 10, 91.0), ('周芷若', 9, 90.0),
# #                                              # ('李莫愁', 33, 0.0), ('小龙女', 23, 0.0))
#
#
#
# # #查询操作，还可以迭代查询
# # # cur游标在查询时可以迭代取值
# # sql = "select name,age,score from class_1;" # 查询数据库的select语句,以字符串的形式，传给execute
# # cur.execute(sql)                            # 执行sql
# #
# # for row in cur:
# #     print(row)
#
#
#
# # # # input输入一个而学生的姓名查询这个学生信息
# # name = input("输入查询的学生姓名：")
# #         # 在sql语句里，where查询名字的时候，名字就要用引号，所以这里也要用引号，
# #         #如果输入的是id，就不要引号，因为sql语句里，id就不要引号,
# #         #不管什么数据类型，都用%s，因为整个sql语句要变成字符串传递给execute
# # sql = "select * from class_1 where name='%s';" % (name)
# # print(sql)  # 可以打印出sql语句，可以在mysql里执行看看，看看语句写的对不对
# # cur.execute(sql)
# # for row in cur:
# #     print(row)
#
#
# # # 上面要不要带引号的问题，比较烦，可以利用execute参数列表解决
# # name = input("输入查询的学生姓名：")
# # sql = "select name,age,score from class_1 where name=%s or score>%s;"
# # cur.execute(sql,[name,90])  # 执行sql,列表不能传递关键字，符号，表名，字段名
# # for row in cur:
# #     print(row)
#
#
#
#
#
# # 对数据库写【增删改】操作
# # try:
# #     sql = "insert into class_1 values (11,'Eva',18,'w',86);"
# #     cur.execute(sql)
# #
# #     sql = "update hobby set price=%s where name =%s;"
# #     cur.execute(sql,[8800,'Joy'])
# #
# #     sql = "delete from hobby1 where name=%s;"
# #     cur.execute(sql, ["lily"])
# #
# #     db.commit()         # 提交，将sql语句的操作行为提交写入到数据库，如果不commit，则程序执行结束后，才会写入到数据库，类似文件读写的缓冲区
# #                         # 上面可以执行多次sql语句，最后一次commit提交
# #
# # except Exception as e:
# #     print(e)
# #     db.rollback()   # 假如上面的sql语句执行出现异常，例如表名不存在，主键重复，sql语句格式问题等等，
# #                     # 则直接rollback，没有提交到数据库的内容，全部失效
# #                     # 如果是不支持事务的引擎，执行一条语句就会直接写入到数据库内这样就不能回滚了，
# #                     #但是支持事务的引擎，则可以回滚，因为数据会保留在事务缓存中。
# #                     #但是这只是理论上如此，有时候即使回滚了，但是有可能遇到缓存刷新，数据也有可能写进去了
#
#
#
#
# # ##批量执行写操作【增删改】
# # # 例如插入多条记录，格式必须是列表嵌套元组，或者列表嵌套列表
# # l = [
# #     ("Dava",16,'m',77),
# #     ("Levi",17,'m',67),
# #     ("Han",18,'w',82)
# # ]
# #
# #
# # try:
# #     sql = "insert into class_1 (name,age,sex,score) values (%s,%s,%s,%s);"
# #
# #     # for i in l:                 #遍历列表，多次执行execute，把列表嵌套的元组的值，带入到insert语句
# #     #     cur.execute(sql,i)
# #
# #     #或如下，效果同上
# #     cur.executemany(sql,l)
# #
# #     db.commit() # 提交，将sql语句的操作行为提交写入到数据库
# # except Exception as e:
# #     print(e)
# #     db.rollback() # 没有提交到数据库的内容，全部失效
# #
#
#
#
#
# # 关闭游标和数据库
# cur.close()
# db.close()
#



'''

练习： 

创建一个而数据库dict,  
 create database dict character set utf8;
 
里面创建一个数据表words ,  字段:id   word  mean
create table words (
    id int primary key auto_increment,
    word varchar(30) not null,
    mean text
);

写代码，将dict.txt单词本中的所有单词和解释插入到对应数据库字段中

'''
#
# import pymysql
#
# db = pymysql.connect(host="localhost",
#                      port=3306,
#                      user='work',
#                      password='123',
#                      database='dict',   #指定数据库名字
#                      charset='utf8'
#                      )
#
# cur = db.cursor()
#
#
# # 对数据库操作 （增删改查）
# f = open("/root/PycharmProjects/pythonProject/阶段02/dict.txt",'r')
#
# for line in f:
#     w = line.split(' ', 2)
#     try:
#         sql = "insert into words(word,mean) values (%s,%s);"   #指定表名字
#         cur.execute(sql, [w[0],w[-1]])
#         db.commit()
#
#     except Exception as e:
#         print(e)
#         db.rollback()
#
# f.close()
#
#
# cur.close()
# db.close()
#

###或者如下

# import re
# import pymysql
#
# # 打开单词本
# f = open("dict.txt")
#
# # 目标是使用一个大列表，每个元素是一个元组，每个元组是单词、解释，[(word,mean),(word,mean)...] ，进而使用executemany
# args_list = []
# for line in f:
#     result = re.findall(r"(\w+)\s+(.*)",line)    # result --> [(work,mean)]
#     args_list.append(result[0])                  #把列表的元组追加给大列表
# f.close()
#
#
# db = pymysql.connect(host="localhost",
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      database='dict',
#                      charset='utf8'
#                      )
#
#
# cur = db.cursor()
#
#
# try:
#     sql = "insert into words (word,mean) values (%s,%s);"
#     cur.executemany(sql,args_list)
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()
#
#
#
# cur.close()
# db.close()
#





'''

文件存储
    即把文件，存储在数据库里

存储文件路径：
    即把文件的路径，存储在数据库里，存的是个路径字符串
优点：节省数据库空间，提取方便
缺点：文件或者数据库发生位置迁移会导致文件丢失

存储文件本身【二进制】
优点：安全可靠，数据库在，文件就在
缺点：占用数据库空间大，文件存取效率低

'''




"""


存取二进制数据


"""

# 在表里增加一个二进制字段，用于存二进制数据本身
# alter table class_1 add image longblob;


# import pymysql
#
# # 连接数据库 (连接自己计算机可以不写host port)
# db = pymysql.connect(host="localhost",
#                      port=3306,
#                      user='work',
#                      password='123',
#                      database='stu',
#                      charset='utf8'
#                      )
#
# # 创建游标 (游标对象负责调用执行sql语句，操作数据，得到结果)
# cur = db.cursor()
#
# #图片存到数据库
# with open('风景.jpeg','rb') as f:
#     data = f.read()  # 二进制读取图片
# sql = "update class_1 set image=%s where id=4;"   #存到数据库
# cur.execute(sql,[data])
# db.commit()
#
# #从数据库提取图片
# sql = "select image from class_1 where id=4;"
# cur.execute(sql)
# data = cur.fetchone()
# with open('sg.jpeg','wb') as f:   #二进制打开一个新文件，写入查询到的元组的元素,
#                                   # 则当前目录下就产生这个新文件了，可以图形界面打开看到图片了
#     f.write(data[0])
#
#
# # 关闭游标和数据库
# cur.close()
# db.close()

