
"""
    面向对象的思考步骤：
    现实事物  -抽象化成->  类  -具体化成-> 对象


"""

"""
定义老婆这个类，
    里面包含名词性的描述，比如名字、工资、颜值等【数据封装】
    里面包含动词性的功能，比如工作内容等
    
然后通过类，创建对象老婆01
然后老婆01，调用类里的动作性函数
"""
# class Wife:  #类名，多个单词的首字母大写，不用下划线隔开
#     # 数据：名词性的描述
#     def __init__(self, name, face_score, money=0.0):
#         self.name = name
#         self.money = money
#         self.face_score = face_score
#
#     # 行为：动词性的功能
#     def work(self):
#         print(self.name, "工作")
#
#
#
# # 创建对象(自动调用__init__函数)
# w01 = Wife("双儿", 979, 2000)
# # 对象w01，调用类里的函数work，自动传递对象w01作为参数，类似 work(w01)
# w01.work()
# #内置函数，以字典的方式，查看对象的所有实例变量和对应的值，
# print(w01.__dict__)
#





"""
对象，                                 也叫实例
对象里的，数据：名词性的描述，即对象的变量，也叫实例变量
对象里的，行为：动词性的功能，即对象的函数，也叫实例方法【实例方法，用于操作实例变量】
"""








"""
    创建手机类
        数据：品牌、价格、颜色
        行为：通话
        
        实例化两个对象
        并调用其函数,   画出内存图
 """
# class Phone:
#     def __init__(self, brand, price, color):
#         self.brand = brand
#         self.price = price
#         self.color = color
# 
#     def call(self):
#         print(self.brand, self.price, self.color, "我在打电话呢！")
# 
# 
# phone01 = Phone("华为", 10000, "白色")
# phone01.call()
# 
# phone02 = Phone("苹果", 15000, "金色")
# phone02.call()
# 







"""
    创建狗类
        数据：品种、爱称、年龄、体重
        行为：吃、叫
        实例化两个对象并调用其方法
"""
# class Dog :
#     def __init__(self, variety, nickname, age, weight):
#         self.variety=variety
#         self.nickname=nickname
#         self.age=age
#         self.weight=weight  # 假如这个参数，形参位置没写，则alt+回车，选择creat参数，则自动添加上形参
#
#
#     def eat(self):
#         print("%s喜欢吃"%(self.nickname))
#
#     def call(self):
#         print("%s喜欢叫" % (self.nickname))
#
# dog01=Dog("金毛","大黄",5,50)
# dog02=Dog("哈士奇","大黑",8,80)
#
# dog01.eat()
# dog01.call()
#
# dog02.eat()
# dog02.call()











"""
列表的元素，是通过类，创建的对象
 """
#
# class Phone:
# 	def __init__(self, brand, price, color):
# 		self.brand = brand
# 		self.price = price
# 		self.color = color
#
# # 列表的元素，是通过类，创建的对象
# list_phones = [
# 	Phone("华为1", 5999, "蓝色"),
# 	Phone("华为2", 6999, "红色"),
# 	Phone("苹果1", 9999, "金色"),
# 	Phone("苹果2", 7999, "白色"),
# 	Phone("三星2", 4999, "白色"),
# ]
#
# #遍历列表里的元素，指向的每个通过类，创建的对象
# for item in list_phones:
# 	if item.color == "白色":
# 		item.price = 0
# print(list_phones[0].price)  # 第一个对象的价格
# print(list_phones[-1].price) # 最后一个对象的价格
#
#
#
# def find():
# 	for item in list_phones:
# 		if item.brand == "华为2":
# 			return item             #返回brand==华为2的整个对象，即Phone("华为2", 6999, "红色")
# result = find()
# print(result.brand,result.price,result.color)#
















"""

类变量：
def函数之外的变量,叫 类变量
使用方式是，         类名.类变量



"""

# class ICBC:
#     total_money = 1000000 # 类变量：总行的钱
#
#     @classmethod                  #类方法的固定格式
#     def print_total_money(cls):   #类方法的参数是类，固定格式是cls
#         print("总行的钱是",cls.total_money)   #类方法里，调用类变量，类方法，就是用来操作类变量的
#
#     def __init__(self, name="", money=0):
#         self.name = name   # 实例变量：支行名字
#         self.money = money # 实例变量：支行的钱
#         ICBC.total_money -= money # 调用类变量，每创建一个对象，总行的钱都会减少一次
#
#
# tt = ICBC("天坛支行", 100000)
# trt = ICBC("陶然亭支行", 300000)
#
# ICBC.print_total_money()#类名，调用类方法，效果类似print_total_money(ICBC)









"""

        统计Wife类创建了多少对象：
            w01 = Wife("建宁")
            w02 = Wife("双儿")
            w03 = Wife("苏荃")
            
            Wife.print_count() # 3
            
        需要在类里，使用计数器【类变量】
        然后使用类方法，调用类变量，即计数器
"""
# class Wife:
#     count = 0
#
#     @classmethod
#     def print_count(cls):
#         print("创建了老婆的数量是：" + str(cls.count))
#
#     def __init__(self, name, face_score, money=0.0):
#         self.name = name
#         self.money = money
#         self.face_score = face_score
#         Wife.count += 1
#
#
# w01 = Wife("双儿", 979, 2000)
# w02 = Wife("三儿", 979, 2000)
# w03 = Wife("四儿", 979, 2000)
#
# Wife.print_count()
















"""
   练习:创建类，列表里的元素，是通过类创建的对象
"""
# class Commodity:
#     def __init__(self, cid, name, price):
#         self.cid = cid
#         self.name = name
#         self.price = price
#
#
# class Order:
#     def __init__(self, cid, count):
#         self.cid = cid
#         self.count = count
#
#
# list_commodity_infos = [
#     Commodity(1001, "屠龙刀", 10000),
#     Commodity(1002, "倚天剑", 10000),
#     Commodity(1003, "金箍棒", 52100),
#     Commodity(1004, "口罩", 20),
#     Commodity(1005, "酒精", 30),
# ]
#
# list_orders = [
#     Order(1001, 1),
#     Order(1002, 3),
#     Order(1005, 2),
# ]

# 1.定义函数,打印所有商品信息,
# def print_all():
#     for item in list_commodity_infos:
#         print("编号%d，名字%s，价格%d"%(item.cid,item.name,item.price))
# print_all()

# # 2. 定义函数,打印商品单价小于2万的商品信息
# def print_less_than_20000():
#     for item in list_commodity_infos:
#         if item.price < 20000:
#             print("编号%d，名字%s，价格%d" % (item.cid, item.name, item.price))
# print_less_than_20000()


# # 3. 查找最贵的商品(使用自定义算法,不使用内置函数)
# def print_max():
#     max = list_commodity_infos[0]
#     for i in range(1, len(list_commodity_infos)):
#         if max.price < list_commodity_infos[i].price:
#             max = list_commodity_infos[i]
#     return max
#
# result=print_max()
# print(result.price)




# # 4. 根据单价对商品列表降序排列
# def descend_order_by_price():
#     for r in range(len(list_commodity_infos) - 1):
#         for c in range(r + 1, len(list_commodity_infos)):
#             if list_commodity_infos[r].price < list_commodity_infos[c].price:
#                 list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]
#
#
# descend_order_by_price()
#
# for item in list_commodity_infos:
#     print(item.__dict__)



# # 5.  定义函数,打印所有订单中的商品信息
# def print_order_all():
#     for oder in list_orders:
#         for commodity in list_commodity_infos:
#             if oder.cid==commodity.cid:
#                 print("编号%d，名字%s，价格%d"%(commodity.cid,commodity.name,commodity.price))
#
# print_order_all()













"""
    私有成员:以双下划线开头的成员【类变量、类方法、实例变量、实例方法】
        类外无法访问,类内可以访问
        本质：障眼法
            看着是双下划线命名  __data
            实际是单下划线类名+双下划线命名 _MyClass__data
"""



"""
    封装行为：

    需求：类的定义者,保障数据的有效性
         例如年龄：  25 ～ 30
         此时年龄这个参数，叫属性property，
         属性可以判断，满足什么条件下，属性可读，可改
   
"""
# class Wife:
#     def __init__(self, name="", age=0, weight=0):
#         self.name = name
#         self.age = age    #这条命令，实际是执行设置函数setter
#         self.weight = weight
#
#     # 如下两段代码，对age这个参数进行了限制25-30之间【此时age一般称为属性】
#     # 函数名age，要跟实例变量age，一样
#     @property    #props+回车，自动跳出语法框架，然后输入函数名age
#     def age(self):    #对象读取age这个参数的时候，执行的是这个读取函数
#         return self.__age
#
#     @age.setter
#     def age(self, value):   #对象修改age这个参数的时候，执行的是这个设置函数
#         if 25 <= value <= 30:
#             self.__age = value
#         else:
#             raise Exception("不行")  #程序报错
#
#     # 如下两段代码，对weight这个参数进行了限制50-60之间
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, value):
#         if 50 <= value <= 60:
#             self.__weight = value
#         else:
#             raise Exception("不行")
#
#
# w01 = Wife("双儿", 25, 70)
# print(w01.name)
# print(w01.age)
# print(w01.weight)


"""
属性只读、只写

"""
# 写法2：只读(只对外提供读取功能,类外不能修改)
# 快捷键：prop + 回车
# class Wife:
#     def __init__(self, age=0):
#         self.__age = age   # 这条命令执行的是设置函数setter，但是没有setter，所以加上__,为私有变量赋值
#
#     @property
#     def age(self):
#         return self.__age
#
# w01 = Wife(25)
# print(w01.age)# 执行读取函数
# w01.age  = 10  #此时修改属性，提示无法设置can't set attribute
#





# 写法3：只写(只能够对外提供设置功能)
# 快捷键： 无
# class Wife:
#     def __init__(self, age=0):
#         self.age = age  # 执行设置函数
#
#     age = property()
#     @age.setter
#     def age(self, value):  # 设置函数
#         self.__age = value
#
#
# w01 = Wife(25)
# print(w01.age)  # 执行读取函数，提示无法读取
# print(w01.__dict__)
















