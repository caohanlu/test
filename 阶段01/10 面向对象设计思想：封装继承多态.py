"""
    面向对象设计思想


    需求：老张开车去东北
    封装：划分类   人类     车类

    变化：增加飞机、自行车....

    以下代码缺点：违反开闭原则
               增加飞机,还要修改人的代码
"""
#
# class Person:
#     def __init__(self, name=""):
#         self.name = name
#
#     def go_to(self,position,vehicle):
#         print(self.name,"去",position)
#         if type(vehicle) == Car:
#             vehicle.run()
#         elif type(vehicle) == Airplane:
#             vehicle.fly()
#
# class Car:
#     def run(self):
#         print("汽车在行驶")
#
# class Airplane:
#     def fly(self):
#         print("飞机在飞行")
#
# # 测试.....
# lw = Person("老王")
# c01 = Car()
# a01 = Airplane()
# lw.go_to("东北",a01)
#










"""
    面向对象设计思想
    
    需求：老张开车去东北
    
    变化：增加飞机、自行车....
    
    封装：划分类   人类     车类
    继承：隔离     人类     具体交通工具
    重写：彰显子类个性   具体交通工具，重写交通工具的方法

    情景：手雷爆炸，可能伤害敌人或者玩家的生命。
    变化：还可能伤害房子、树、鸭子....
    要求：增加新事物，不影响手雷.
    体会：开闭原则
    画出架构设计图

"""
#
# class Person:
#     def __init__(self, name=""):
#         self.name = name
#
#     def go_to(self, position, vehicle):
#         print(self.name, "去", position)
#         vehicle.transport()
#
#
# class Vehicle:
#     """
#         交通工具虽然没有具体功能代码, 但是在隔离人与具体交通工具
#         所有交通工具的函数名，都是用统一的父类的def transport(self)，然后子类重写父类的def transport(self):
#     """
#
#     def transport(self):
#         pass
#
#
# class Car(Vehicle):
#     def transport(self):   #重写父类的函数
#         print("汽车在行驶")
#
#
# class Airplane(Vehicle):
#     # ctrl+o
#     def transport(self):  #重写父类的函数
#         print("飞机在飞行")
#


# 测试.....
# lw = Person("老王")

# c01 = Car()
# a01 = Airplane()

# lw.go_to("东北", c01)








"""
练习
    情景：地雷爆炸，可能伤害敌人或者玩家的生命。
    
    变化：还可能伤害房子、树、鸭子....
    
    要求：增加新事物，不影响手雷.

步骤：
封装、继承、多态【重写】
"""
# class Mine:
#     def boom(self,victim):
#         victim.injure()   #调用父【先用】
#
#
# class Victim:
#     def injure(self):
#         pass
#
# class Tree(Victim):
#     def injure(self):    #子重写【后做】
#         print("树受伤")
#
# class House(Victim):     #子重写【后做】
#     def injure(self):
#         print("房子受伤")
#
#
#
# mine01=Mine()
#
# tree01=Tree()            #创建子
# house01=House()
#
# mine01.boom(tree01)
# mine01.boom(house01)













"""
    多态【重写】
        定义：父类的同一种动作或者行为，在不同的子类上有不同的实现。
        步骤：
            1. 调用父
            2. 子重写
            3. 创建子
        目的：
            彰显子类个性(不同/变化/具体)
            体现开闭原则(目标)
"""
#
# def func02(a):
#     # 1. 调用父
#     a.func01()
#
#
# class A:
#     def func01(self):
#         pass
#
# class B(A):
#     # 2. 子重写
#     def func01(self):
#         print("B -- func01")
#
# class C(A):
#     def func01(self):
#         print("C -- func01")
#
#
# # 3. 创建子
# b = B()
# c = C()
#
# func02(c)









"""
练习
    创建图形管理器
	1. 记录多种图形（圆形、矩形....）
	2. 提供计算总面积的方法.
    满足：
        开闭原则
    测试：
        创建图形管理器，存储多个图形对象。
        通过图形管理器，调用计算总面积方法.

    三大特征
        封装成类：创建图形管理器类，圆形类，矩形类
        继承：创建圆形类，矩形类的父类，即图形类   (抽象/统一/隔离 具体图形)
        多态: 图形管理器类，调用父类的计算图形面积的方法
             圆形类，矩形类，重写父类的计算图形面积的方法
              向图形管理器类里，添加圆形类，矩形类的对象
    六大原则：
        开闭：增加新图形,图形管理器不变.
        单一职责：
            GraphicManager管理所有图形
            Circle 计算圆形面积
            Rectanle 计算矩形面积
        依赖倒置：GraphicManager使用父Graphic
        组合复用：GraphicManager与图形

"""

#
#
# class GraphicManager:
#     def __init__(self):
#         self.all_graphic = []             #因为需要记录多个图形，所以搞个列表
#
#     # graphic 类型是父类图形
#     def add_graphic(self,graphic):
#         self.all_graphic.append(graphic)   #把圆形、矩形的对象，添加到列表
#
#     def calculate_total_area(self):
#         total_area = 0
#         for graphic in self.all_graphic:
#             total_area += graphic.get_area()    #圆形、矩形的对象，调用父类的get_area()方法，但是改方法被改写了
#         return total_area
#
# class Graphic:
#     def get_area(self):
#         pass
#
# # 父类在约束所有所有子类在某一行为上达到统一
# class Circle(Graphic):
#     def __init__(self,r):
#         self.r = r
#
#     def get_area(self):
#         # 重写
#         return 3.14 * self.r ** 2
#
# class Rectanle(Graphic):
#     def __init__(self, l,w):
#         self.l = l
#         self.w = w
#
#     def get_area(self):
#         return self.l * self.w
#
# manager = GraphicManager()
# manager.add_graphic(Circle(5))
# manager.add_graphic(Rectanle(5, 6))
# print(manager.calculate_total_area())









"""
    创建员工管理器
        1. 记录多个员工（程序员、测试员....）
        2. 提供计算总薪资的方法.

    程序员：底薪 + 项目分红
    测试员: 底薪 + Bug数 × 5

    满足：
        开闭原则
    测试：
        创建员工管理器，存储多个员工对象。
        通过员工管理器，调用计算总薪资方法.


    三大特征
        封装：创建员工管理器这个类，程序员类，测试员类
        继承：创建程序员类，测试员类的父类，即员工类
        多态:员工管理器类调用父类的计算员工工资的方法
            子类重写父类的计算员工工资的方法
            向员工管理器类添加的是子类的对象

    六大原则：
        开闭：增加新岗位的员工，EmployeeManager不改变
        单一职责：
            EmployeeManager操作所有员工
            Programmer负责实现程序员的薪资算法
            Tester负责实现测试员的薪资算法
        依赖倒置：
            EmployeeManager使用Employee
            不使用Programmer、Tester
        组合复用：
            EmployeeManager和员工薪资算法
        里氏替换：
            Programmer、Tester重写时先调用父类方法
        迪米特法则：
            Employee隔离EmployeeManager与Programmer、Tester的变化
"""

# class EmployeeManager:
#     def __init__(self):
#         self.all_employee = []      #由于要记录多个员工，所以搞个列表
#
#     def add_employee(self, emp):
#         self.all_employee.append(emp)  #把子类创建出来的程序员、测试员的对象，追加到列表
#
#     def calculate_total_money(self):
#         total_money = 0
#         for emp in self.all_employee:
#             total_money += emp.get_money()  #调用程序员、测试员的对象的，改写后的get_money()方法
#         return total_money
#
#
# class Employee:
#     def get_money(self):
#         pass
#
#
#
#
# class Programmer(Employee):
#     def __init__(self, base_salary, bonus):
#         self.base_salary = base_salary
#         self.bonus = bonus
#
#     def get_money(self):
#         return self.base_salary + self.bonus
#
#
# class Tester(Employee):
#     def __init__(self, base_salary, bug_count):
#         self.base_salary = base_salary
#         self.bug_count = bug_count
#
#     def get_money(self):
#         return self.base_salary + self.bug_count * 5
#
#
# manager = EmployeeManager()
# manager.add_employee(Programmer(8000, 100000))
# manager.add_employee(Tester(5000, 500))
# print(manager.calculate_total_money())



#上面的代码,可以优化下细节
# class EmployeeManager:
#     def __init__(self):
#         self.__all_employee = []   # 建议将使用的数据私有化
#
#     def add_employee(self, emp):
#         if isinstance(emp, Employee):  # 如果 emp  是一种 员工类型，再追加到列表
#             self.__all_employee.append(emp)
#
#     def calculate_total_money(self):
#         total_money = 0
#         for emp in self.__all_employee:
#             total_money += emp.get_money()
#         return total_money
#
#
# class Employee:
#     def __init__(self, base_salary):  #由于所有员工都有底薪，所以父类可以增加底薪这个参数
#         self.base_salary = base_salary
#
#     def get_money(self):
#         return self.base_salary      #返回底薪
#
#
#
# class Programmer(Employee):
#     def __init__(self, base_salary, bonus):
#         super().__init__(base_salary)     #调用父类的构造函数，并且传递底薪参数
#         self.bonus = bonus
#
#     def get_money(self):
#         base_salary = super().get_money()  # 先通过爸爸的方法获取底薪
#         return base_salary + self.bonus    #再底薪加上分红
#
#
# class Tester(Employee):
#     def __init__(self, base_salary, bug_count):
#         super().__init__(base_salary)
#         self.bug_count = bug_count
#
#     def get_money(self):
#         return super().get_money() + self.bug_count * 5
#
#
# manager = EmployeeManager()
# manager.add_employee(Programmer(8000, 100000))
# manager.add_employee(Tester(5000, 500))
# manager.add_employee("二大爷")
# print(manager.calculate_total_money())
#








"""
练习：多个类之间，需要互相调用，使用父类隔离：
    
    
    
    玩家、敌人，都有血量、攻击力两个参数,被攻击时候，血量要减去对方的攻击力
    
    玩家攻击敌人(掉装备),还可能死亡(播放死亡动画)
    敌人攻击玩家(碎屏),还可能死亡(游戏结束)
    
    要求：增加其他角色参与战斗,玩家和敌人类代码不变.
    
    
    
    
    三大特征
    封装：创建玩家类、敌人类
    继承：创建玩家类、敌人类的父类，即游戏角色类
                                父类的函数：攻击、受伤、死亡
    多态: 子类重写父类的受伤、死亡方法
        

"""

#
# class Character:
#     def __init__(self, hp=0, atk=0):
#         self.hp = hp
#         self.atk = atk
#
#     # 所有子类完整共性(子类不用重写)
#     def attack(self, target):
#         print("打你")
#         # 1. 调用父
#         target.damage(self.atk)
#
#     # 所有子类部分共性(子类重写需要通过super调用父)
#     def damage(self, value):
#         self.hp -= value
#         if self.hp <= 0:
#             self.death()
#
#     # 所有子类行为共性(没有实现共性,子类重写)
#     def death(self):
#         pass
#
#
# class Player(Character):
#     # 2. 子重写
#     def damage(self, value):
#         print("碎屏")
#         super().damage(value)
#
#     def death(self):
#         print("游戏结束")
#
#
# class Enemy(Character):
#     def damage(self, value):
#         print("掉装备")
#         super().damage(value)
#
#     def death(self):
#         print("播放死亡动画")
#
# # 3. 创建子
# p01 = Player(100, 50)
# e01 = Enemy(50, 30)
# e01.attack(p01)
# p01.attack(e01)
#
#
