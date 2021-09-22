
"""
    类与类之间的调用：
        需求：老张开车去东北

            类：承担行为   【行为一样的，划分成一个类】【按照行为，划分成类，就叫做封装】
            对象：承担数据 【每个对象的数据不一样，但是每个对象的行为是一样的】

         1. 识别对象
            老张           车
         2. 分配职责
                去()         行驶()
         3. 建立交互
            老张调用车
         4.东北没有动作，所以不用划分成类

"""


# 写法1：直接创建对象
# 语义： 老张去东北用一辆新车
# class Person:
#     def __init__(self, name=""):
#         self.name = name
#
#     def go_to(self, position):
#         print(self.name, "去", position)
#         car = Car()  # 调用类Car()，创建了对象car
#         car.run()  # 对象car，调用了类Car()里的函数run
#                     #这种写法，每去一个地方，都会执行一次car = Car()，即都会创建一个car对象，不太合适
#
#
# class Car:
#     # 实例方法
#     def run(self):
#         print("汽车在行驶")
#
#
# lw = Person("老王")
# lw.go_to("东北")
# lw.go_to("西北")


# 写法2：在构造函数中创建对象
# 语义： 老张开车自己的车去东北
# class Person:
#     def __init__(self, name=""):
#         self.name = name
#         self.car = Car()   #在构造函数中，通过类class Car，创建对象car
#
#     def go_to(self, position):
#         print(self.name, "去", position)
#         # 第一次.: 从栈帧到人对象
#         # 第二次.: 从人到车对象
#         self.car.run()    #通过self.car调用实例方法run()
#
#
# class Car:
#     # 实例方法
#     def run(self):
#         print("汽车在行驶")
#
#
# lw = Person("老王")
# lw.go_to("东北")
# lw.go_to("西北")


# 写法3：通过参数传递对象
# 语义：人通过交通工具(参数传递而来)去东北
# class Person:
#     def __init__(self, name=""):
#         self.name = name
#
#     def go_to(self, position, vehicle): #vehicle是参数名
#         print(self.name, "去", position)
#         vehicle.run()   #vehicle是参数名，vehicle这个对象，调用函数run()
#
#
# class Car:
#     # 实例方法
#     def run(self):
#         print("汽车在行驶")
#
#
# lw = Person("老王")
# c01 = Car()
# lw.go_to("东北", c01)#c01这个Car对象，通过参数，传递给go_to函数


"""
练习：
        需求：小明请保洁打扫卫生

         1. 识别对象
            小明【客户类】           保洁【保洁类】
         2. 分配职责
            通知         打扫卫生
         3. 建立交互
            小明调用保洁的打扫卫生方法
"""
# 写法1：类里的动作函数，创建别的类的对象，然后通过对象调用别的类的实例方法
#       每次请一个新保洁
# class Client:
#     def __init__(self, name=""):
#         self.name=name
#     def notify(self):
#         cleaner=Cleaner()
#         cleaner.clean()
#
# class Cleaner:
#     def __init__(self, name=""):
#         self.name=name
#     def clean(self):
#         print("保洁在打扫卫生")
#
# client=Client("小明")
# client.notify()


# 写法2：类里的构造函数，创建别的类的对象，然后通过对象调用别的类的实例方法
# 每次请同一个保洁
# class Client:
#     def __init__(self, name=""):
#         self.name=name
#         self.cleaner=Cleaner()
#     def notify(self):
#         self.cleaner.clean()
#
# class Cleaner:
#     def __init__(self, name=""):
#         self.name=name
#     def clean(self):
#         print("保洁在打扫卫生")
#
# client=Client("小明")
# client.notify()


# 写法3：通过参数，调用别的类的实例方法
# class Client:
#     def __init__(self, name=""):
#         self.name=name
#     def notify(self,cleaner):
#         cleaner.clean()
#
#
# class Cleaner:
#     def __init__(self, name=""):
#         self.name=name
#     def clean(self):
#         print("保洁在打扫卫生")
#
# client=Client("小明")
# cleaner01=Cleaner()
# client.notify(cleaner01)


"""
练习
    1. 玩家攻击敌人,敌人受伤(播放动画)
    2. 玩家(攻击力)攻击敌人(血量),
        敌人受伤(播放动画,血量减少)
    3. 敌人(攻击力)还能攻击玩家(血量),
        玩家受伤(碎屏,血量减少)
"""
#
#
# class GamePlayer:
#     def __init__(self, name="", power=0, blood=0):
#         self.name = name
#         self.power = power
#         self.blood = blood
#
#     def attack(self, enemy):
#         enemy.injured(self.power)
#
#     def injured(self, value):
#         print("玩家受伤")
#         self.blood -= value
#         print(self.blood)
#
#
# class Enemy:
#     def __init__(self, name="", power=0, blood=0):
#         self.name = name
#         self.power = power
#         self.blood = blood
#
#     def attack(self, gameplayer):
#         gameplayer.injured(self.power)
#
#     def injured(self, value):
#         print("敌人受伤了")
#         self.blood -= value
#         print(self.blood)
#
#
# gameplayer01 = GamePlayer("玩家01", 10, 100)
# enemy01 = Enemy("敌人01", 10, 100)
# gameplayer01.attack(enemy01)
# enemy01.attack(gameplayer01)


"""
    继承

        编程：代码不用子类写，但是子类能使用
        多个类有代码的共性，且属于共同一个概念。

    下面继承父类的实例方法【即函数】
"""

# 从思想讲：先有子再有父
# 从编码讲：先有父再有子


# 多个类有代码的共性，且属于共同一个概念。
# 比如学生会说话，老师也会说话，则把说话这段代码 抽象成人这个类，人会说话
# class Person:
#     def say(self):
#         print("说话")
#
# class Student(Person):  #(Person)，表示继承父类Person
#     def study(self):
#         self.say()      #可以调用父类的实例方法
#         print("学习")
#
# class Teacher(Person):
#     def teach(self):
#         print("教学")
#
#
# # 创建子类对象,可以调用父类方法和子类方法
# s01 = Student()
# s01.say()   #这个就是父类方法
# s01.study()
#
# # 创建父类对象,只能调用父类方法
# p01 = Person()
# p01.say()


"""
父类、子类，关系的判断方法，三种
【兼容性判断】
"""
#
# # isinstance(对象,类)  判断关系，python内置函数
#
# # 学生对象  是一种  学生类型
# print(isinstance(s01, Student)) # True
# # 学生对象  是一种  人类型
# print(isinstance(s01, Person)) # True
# # 学生对象  是一种  老师类型
# print(isinstance(s01, Teacher)) # False
# # 人对象  是一种 学生类型
# print(isinstance(p01, Student)) # False
#
#
#
#
# # issubclass(类型,类型)  判断关系
#
# # 学生类型  是一种  学生类型
# print(issubclass(Student, Student)) # True
# # 学生类型  是一种  人类型
# print(issubclass(Student, Person)) # True
# # 学生类型  是一种  老师类型
# print(issubclass(Student, Teacher)) # False
# # 人类型  是一种 学生类型
# print(issubclass(Person, Student)) # False
#
#
#
#
#
# # Type
# # type(对象) == 类型  相等/相同/一模一样
#
# # 学生对象的类型  是  学生类型
# print(type(s01) == Student) # True
# # 学生对象的类型  是  人类型
# print(type(s01) == Person) # False
# # 学生对象的类型  是  老师类型
# print(type(s01) == Teacher) # False
# # 人对象的类型    是  学生类型
# print(type(p01) ==  Student) # False


"""
    继承数据【继承的是父类的实例变量】

        class 儿子(爸爸):
            def __init__(self, 爸爸构造函数参数,儿子构造函数参数):
                super().__init__(爸爸构造函数参数)
                self.数据 = 儿子构造函数参数
"""

# class Person:
#     def __init__(self, name="", age=0):
#         self.name = name
#         self.age = age
#
#
# class Student(Person):
#     def __init__(self, name="", age=0, score=0):
#         super().__init__(name, age) # 通过super()调用父类__init__函数，自己的__init__需要给父类的__init__传递参数
#         self.score = score
#
#
# # 1. 子类可以没有构造函数,可以直接使用父类的__init__函数
# s01 = Student()
#
# # 2. 子类有构造函数,会覆盖父类构造函数(好像他不存在)
# #    所以子类必须通过super()调用父类构造函数
# s01 = Student("小明", 24, 100)
# print(s01.name)
# print(s01.age)
# print(s01.score)
#


"""
练习：继承数据【即继承实例变量】

    创建父类：车(品牌，速度)
    创建子类：电动车(电池容量,充电功率)
    创建子类对象并画出内存图。
"""
# class Car:
#     def __init__(self, brand="", speed=0):
#         self.brand=brand
#         self.speed=speed
#
# class ElectricVehicle(Car):
#     def __init__(self,brand="", speed=0,capacity=0,power=0):
#         super().__init__(brand,speed)
#         self.capacity=capacity
#         self.power=power
#
# ElectricVehicle01=ElectricVehicle("速派奇",100,200,200)
# print(ElectricVehicle01.brand)
# print(ElectricVehicle01.speed)
# print(ElectricVehicle01.capacity)
# print(ElectricVehicle01.power)










"""
    多继承
         同名方法解析顺序
            类.mro()
"""

#
# class A:
#     def func01(self):
#         print("A -- func01")
#
#
# class B(A):
#     def func01(self):
#         print("B -- func01")
#
#
# class C(A):
#     def func01(self):
#         print("C -- func01")
#
#
# class D(B, C):
#     def func01(self):
#         super().func01()  # 继承列表第一个父类B的func01()方法
#         print("D -- func01")
#
#
# d = D()
# d.func01()


# 具体的解析顺序：使用 类名字.mro()方法，可以print出来
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# print(D.mro())

