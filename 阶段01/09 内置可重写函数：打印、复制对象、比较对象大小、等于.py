"""
    内置可重写函数
    def __str__(self)   打印对象
    def __repr__(self)  复制对象
"""


# 任何一个类,都直接或间接继承自object类(万类之祖).




# class Dog:    # 类似class Dog(object):
#     def __init__(self, variety, name, age, weight=0.0):  # 时机：创建对象时
#         self.variety = variety
#         self.name = name
#         self.age = age
#         self.weight = weight
#
#     def __str__(self):  # 时机：打印对象时    # return部分，没有语法限制，对人友好，     将对象转换成字符串
#         return f"我是{self.name},品种{self.variety},今年{self.age}岁了,体重{self.weight}斤"
#
#     def __repr__(self): # 时机：拷贝对象时
#                         # return部分，return的是一条创建对象的代码，该代码以字符串的格式return出来
#                         # 所以要写成Python语法格式，解释器可识别
#                         #加双引号，是因为创建对象时，对象里的参数，如果是字符串，要加双引号
#         return f'Dog("{self.variety}", "{self.name}", {self.age}, {self.weight})'



# d01 = Dog("拉布拉多", "米咻", 5, 70)


#print(d01)   #打印狗对象的时候，会自动执行如下两行代码
# message = d01.__str__()   #__str__()是内置可重写函数，类似__init__，可以按照需要，改成我们想要的代码
# print(message)



#d02是字符串   “Dog("拉布拉多", "米咻", 5, 70)”
# d02=d01.__repr__()   #__repr__()是内置可重写函数，类似__init__，可以按照需要，改成我们想要的代码
# print(d02)


# 将字符串作为代码执行
# eval(字符串)  --> eval(input()) 将"无所不能"
# d02 = eval(d01.__repr__())
# print(d02)


#对象复制后，修改其中一个对象，不会影响另一个对象










"""
练习
    1. 打印下列类的对象
        xx车的速度是xx
    2. 拷贝下列类的对象,
       修改拷贝前对象实例变量,
       打印拷贝后对象.
"""

# class Car:
#     def __init__(self, bread="", speed=0):
#         self.bread = bread
#         self.speed = speed
#
#     def __str__(self):
#         return "%s车的速度是%d" % (self.bread, self.speed)
#
#     def __repr__(self):
#         return 'Car("%s",%d)' % (self.bread, self.speed)
#
#
# c01 = Car("奥迪", 100)
# print(c01)
#
# c02 = eval(c01.__repr__())
# print(c02)
#
# c01.bread = "华为"
# print(c01)
# print(c02)











"""
    运算符重载
        算数运算符  + - * / ...
"""

# class Vector2:
#     """
#         二维向量
#     """
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):#由于是两个向量相加，所以相加后的结果，也应该是个向量，所以写成如下格式
#         return Vector2(self.x + other.x, self.y + other.y)
#
#
# pos01 = Vector2(1, 2)
# pos02 = Vector2(3, 4)
#
# pos03 = pos01 + pos02  #pos01对象，调用自己的add函数，并且传递参数pos02，类似 pos01.__add__(pos02)
# print(pos03.__dict__)
#











"""

    运算符重载
    
        
        + 无论可变还是不可变对象,都创建新对象

        += 对于可变对象,在原有基础上进行修改
           对于不可变对象,创建新对象
           增强运算符 +=  -=  *=  /=   ...


# +=   对于可变对象,在原有基础上进行修改
list01 = [1]
print(id(list01))# 139887136870152
list01 += [2]
print(id(list01))# 139887136870152


# +=   对于不可变对象,创建新对象
tuple01 = (1,)
print(id(tuple01))# 139887167310872
tuple01 += (2,)
print(id(tuple01))# 139887136858376
"""

# class Vector2:
#     """
#         二维向量
#     """
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     # +=
#     def __iadd__(self, other):
#         self.x += other.x
#         self.y += other.y
#         return self        # 因为自定义类是可变对象，所以返回原有对象self,不是创建新对象
#
# pos01 = Vector2(1, 2)
# print(id(pos01))
# pos01 += Vector2(3, 4)   #自动调用    def __iadd__(self, other)函数
# print(id(pos01))
#











"""
    练习:自学其他算数运算符与增强运算符重载
          -             -=
          *             *=
        创建新对象     返回原对象
"""
# class Vector2:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
#     def __mul__(self, other):
#         if type(other) == Vector2:
#             x = self.x * other.x
#             y = self.y * other.y
#         else:  # 默认为int类型
#             x = self.x * other
#             y = self.y * other
#         # 返回新对象
#         return Vector2(x, y)
# #
#     def __imul__(self, other):
#         if type(other) == Vector2:
#             x = self.x * other.x
#             y = self.y * other.y
#         else:  # 默认为int类型
#             x = self.x * other
#             y = self.y * other
#         # 返回原对象
#         self.x = x
#         self.y = y
#         return self
#
#
# pos01 = Vector2(1, 2)
# pos02 = Vector2(3, 4)
#
# pos03 = pos01 * pos02  # pos01.__mul__(pos02)
# print(pos03.__dict__)  #
# pos04 = pos01 * 2
# print(pos04.__dict__)  #
#
# pos01 *= pos02
# print(pos01.__dict__)  #
# pos01 *= 2
# print(pos01.__dict__)  #
#
















"""
这个比较常用

    自定义对象的列表,如果需要使用内置函数，就需要重写比较运算符.
    
    重写比较运算符
        __eq__  定义对象、实例变量相同的依据
        __lt__  定义大小依据
        
"""
# class Employee:
#     def __init__(self, eid=0, did=0, name="", money=0):
#         self.eid = eid
#         self.did = did
#         self.name = name
#         self.money = money
#
#     # 员工对象的相同依据
#     def __eq__(self, other):
#         return self.eid == other.eid
#
#     # 员工对象的大小依据
#     def __lt__(self, other):
#         return self.money < other.money     #按照money变量，从小到大


# e01 = Employee(1001, 9002, "师父", 60000)
# e02 = Employee(1001, 9002, "师父", 60000)
#
#



# # == ，内部调用__eq__函数，比较两个对象内容是否相同
# print(e01 == e02) # true  因为上面重写了对象相同的依据是eid相同，编号相同，类似e01.__eq__(e02)
# # 比较两个对象地址是否相同
# print(e01 is e02) # false 两个员工对象



# 员工列表
# list_employees = [
#     Employee(1001, 9002, "师父", 60000),
#     Employee(1001, 9002, "师父", 60000),
#     Employee(1001, 9002, "师父", 60000),
#     Employee(1002, 9001, "孙悟空", 50000),
#     Employee(1003, 9002, "猪八戒", 20000),
#     Employee(1004, 9001, "沙僧", 30000),
#     Employee(1005, 9001, "小白龙", 15000),
# ]

#如下命令，写完整应该是print(list_employees.count(1001, 9002, "师父", 60000))
#但是由于构造函数的参数都有默认参数，所以只写了eid这个参数
#所以意思就是判断eid是1001的对象，出现的次数，前提是类里写了__eq__这个函数
# print(list_employees.count(Employee(1001)))



 #判断eid是1005的对象，在列表里的索引，前提是类里写了__eq__这个函数
# print(list_employees.index(Employee(1005)))




# list_employees.sort()  # sort函数，调用对象的__lt__方法，按照money变量，从小到大排序
# print(list_employees) # 重写__repr__,或者这里加断点debug，可以看到排序后的列表
#















"""
练习
"""


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.cid == other.cid

    def __lt__(self, other):
        return self.price < other.price

list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]
# 1. 在商品列表中,查找Commodity(1003)的索引  列表.index   #def __eq__
# print(list_commodity_infos.index(Commodity(1003)))


# # 2. 在商品列表中,判断是否存在Commodity(1005)的商品 Commodity(1005) in 列表   # #def __eq__
# print(Commodity(1005) in list_commodity_infos)


# # 3. 在商品列表中,移除Commodity(1002)对象   列表.remove    # #def __eq__
# list_commodity_infos.remove(Commodity(1002))



# 4. 在商品列表中,根据单价升序排列    列表.sort     #def __lt__
# list_commodity_infos.sort()
# print(list_commodity_infos)



# 5. 在商品列表中,获取单价最高的商品   max(列表)    #def __lt__
# print(max(list_commodity_infos).__dict__)