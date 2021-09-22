"""
    模块【即python文件】

    练习：
        将student_info_manager.py分解为4个模块
            -- bll.py --> 业务business 逻辑logic 层layer
                          存储Controller类
            -- usl.py --> 用户user 显示show 层layer
                          存储View类
            -- model.py --> 存储数据模型Model
            -- main.py  --> 存储入口代码
"""



# 建议设置项目根目录，将需要互相调用的多个py文件、和包的共同文件夹，比如day14
#  -- 在day14文件夹上,右键选择"Mark Directory as"
#  -- 在选择"Sources Root"，进行标蓝，这样多个文件互相导入的时候，有提示信息
#一个项目里，建议只标蓝一个文件夹否则有可能导入的是别的蓝文件夹里的文件，别的蓝文件夹unmark Sources Root

#alt+回车，自动导入，一般开发的时候，都是这样导入
#模块被导入时，所有代码都会执行一次，如果同一个模块导入另一个模块，导入多次，则只执行一次





# 导入方式1： 创建变量module01关联该模块
# 语法：
# import 模块
# 模块.成员
# 适合：面向过程的技术(全局变量、函数)
# 如下，导入module01这个py文件，然后通过文件名module01调用函数func01()
# import module01
# module01.func01()

# m01 = module01.MyClass()
# m01.func02()







# 导入方式2： 将该模块成员导入到当前作用域中
# 语法：from 文件名 import 内容
# 适合：面向对象的技术(类)
#from module01 import func01
# from module01 import MyClass
#
# func01()
#
# m01 = MyClass()
# m01.func02()
#
#快捷键是   alt+回车







# 导入方式3： 将该模块所有成员导入到当前作用域中
# 语法：from 文件名 import *
# 适合：面向对象的技术(类)
# from module01 import *
#
# func01()
#
# m01 = MyClass()
# m01.func02()









"""
这个比较重要



导入包packge【包比文件夹direcory多一个__init__.py文件】下的某模块【python文件】



目录结构：
包、模块调用(文件夹)
    模块(文件)
        类
            函数
                语句


第一次运行的py文件，叫主模块，主模块所在的文件夹，叫真正的项目根目录
"Mark Directory as"标蓝，是设置项目根目录

导入模块是否成功的唯一标准：
    导入路径 + sys.path【是个列表】 = 实际路径
import sys
sys.path.append("/home/tarena/month01/code/day15/my_projcet")
print(sys.path)

标蓝，实际上就是向sys.path这个列表里加路径，
如果不是用pycharm开发而是使用linux命令行执行py文件，有可能需要手动sys.path.append路径
"""


# # 方法1
# # import 路径.模块名

# import package01.package02.module01 as m    #取别名为m    package01为项目根目录下的第一个包
# m.func01()
#




# # 方法2    快捷键依然是alt+回车
# from 路径.模块名 import 成员
# from package01.package02.module01 import func01
# func01()



# 方法3
# from 路径.模块名 import *
# from package01.package02.module01 import *
# func01()





"""
用的比较少

    导入包，而不是导入包下的某个py文件
    
    不管是导入包，还是导入包下的某个文件，在导入的时候，只执行一次包的__init__.py文件
    
    所以需要先设置包的__init__.py文件
    
    假设package01目录下有个包package02，下面有个puthon文件module01
    则导入方式如下
"""
# 方式1：import 包、模块调用
# 设置__init__.py：       import package01.package02.module01
# import package01.package02 as p
# p.module01.func01()


# 方式2：from 包、模块调用 import 包、模块调用
# 设置__init__.py：       from package01.package02 import module01
# from package01 import package02
# package02.module01.func01()


# 方式3：from 包、模块调用 import *
# 设置__init__.py：        __all__ = ["module01"]
# from package01.package02 import *
# module01.func01()











"""

模块变量

"""


# import demo01
# # -- 获取文档字符串,即py文件最上方的三个双引号里的注释信息
# print(demo01.__doc__)
#


# # -- 获取py文件完整路径
# # /home/tarena/2005/day15/demo03.py
# print(demo01.__file__)
#



# # -- 获取模块名称
# print(demo01.__name__) # 被导入的模块的模块名是demo01
# print(__name__) # 只有当前模块是主模块时,才是"__main__"
#
#如下表示，只有当前模块是主模块，才执行入口程序，
# 否则假如main模块被别的模块导入了，此时__name__是main而不是__main__，则不执行入口程序
# if __name__ == '__main__':  #敲main，然后回车，自动跳出这句话
#     view=View()
#     view.main()
#     print("我是主模块")





"""
    对时间的处理
    导入内置模块time
    https://www.runoob.com/python3/python3-date-time.html
"""
# import time
#
# # 1. 人类时间
# # 时间元组: 年/月/日/时/分/秒/星期/一年的第几天/夏令时
# #星期是索引，比如星期2,这里显示的是1
# print(time.localtime())
#
# # 2. 计算机时间
# # 时间戳: 从1970年1月1日 0时0分0秒到现在经过的秒数
# print(time.time())  # 1592377581.6000147
#
# # 3. 时间戳 --> 时间元组
# tuple_time = time.localtime(1592377581.6000147)
# print(tuple_time)
#
# # 4. 时间元组 --> 时间戳
# print(time.mktime(tuple_time))
#
#
# # 5. 时间元组 --> 字符串
# # 语法:字符串 = time.strftime(格式,时间元组)
# # 20/06/17 15:06:21
# print(time.strftime("%y/%m/%d %H:%M:%S",tuple_time))
# # 2020/06/17 15:06:21
# print(time.strftime("%Y/%m/%d %H:%M:%S",tuple_time))
#
#
# # 6. 字符串 --> 时间元组
# # 语法:时间元组 = time.strptime(时间字符串,格式)
# print(time.strptime("2020/06/17 15:06:21","%Y/%m/%d %H:%M:%S"))






"""
    定义函数,根据年月日计算星期数
    结果：星期一
         星期二
         ....
         星期日
         
    步骤:定义函数(函数名称/参数/返回值)
         拼接年月日 --> 字符串   2020-6-17   %Y-%m-%d
         字符串 --> 时间元组
         时间元组  --> 星期
         星期 --> 星期一
"""
# import time
#
#
# def get_week(year, month, day):
#     # str(year) + "-" + str(month) +"-" +str(day)
#     # "%d-%d-%d"%(year, month, day)
#     # f"{year}-{month}-{day}"
#     str_time = f"{year}-{month}-{day}"
#     tuple_time = time.strptime(str_time, "%Y-%m-%d")
#     week_index = tuple_time[6]
#     weeks = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
#     return weeks[week_index]
#
#
# print(get_week(2020, 6, 17))

