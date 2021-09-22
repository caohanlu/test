
"""
    函数式编程
        理论支柱：
            将函数赋值给变量,通过变量调用函数
        应用：
            将函数赋值给参数,通过参数调用函数
            （价值：通过参数调用函数,可以将(核心)逻辑注入到函数中.）
"""

# def func01():
#     print("func01执行了")
#
# # a = func01 # 将函数赋值给变量
# # a()         # 通过变量调用函数
#
#
# def func02():
#     print("func02执行了")
#
#
# def func03(a):     # 价值:通过参数调用函数,可以将(核心)逻辑注入到函数中.
#     print("func03执行了")
#     a()            # 执行参数a对应的函数
#
# func03(func01)     #将func01函数，通过参数a，传递给func03
# func03(func02)     #将func02函数，通过参数a，传递给func03





"""
    函数式编程 - 思想
        面向对象
            封装：分
            继承: 隔
        函数式编程
            分：将变化点分为多个函数，变化点需要的信息，作为参数
            隔: 使用参数隔离具体变化的函数[例如条件]

"""
#
# list01 = [42,45,5,66,7,89]
#
# # 需求：定义函数,获取所有大于10的数字
# def find01():
#     for item in list01:
#         if item > 10:
#             yield item
#
# # 需求：定义函数,获取所有偶数
# def find02():
#     for item in list01:
#         if item % 2 == 0:
#             yield item
#
#
# for number in find01():
#     print(number)
#
# for number in find02():
#     print(number)
#
#
# # －－－－－－－－－－－－－－－－－－
#
# # 提取通用函数 -- 万能查找，根据参数func传递来的查找条件函数，查找满足条件的内容
# def find(func):#　创建了钩子
#     for item in list01:
#         if func(item):# 拉起钩子(执行条件)
#             yield item
#
# # 提取变化函数
# def condition01(item):
#     return item > 10
#
# def condition02(item):
#     return item % 2 == 0
#
#
# for number in find(condition01):# 向钩子上挂条件
#     print(number)
#
# for number in find(condition02):# 向钩子上挂条件
#     print(number)
#
#
#
#


"""

练习

"""
# class EmployeeModel:
#     def __init__(self, eid=0, did=0, name="", money=0.0):
#         self.eid = eid
#         self.did = did
#         self.name = name
#         self.money = money
#
#
# list_employee = [
#     EmployeeModel(1001, 9003, "林玉玲", 13000),
#     EmployeeModel(1002, 9005, "王荆轲", 16000),
#     EmployeeModel(1003, 9003, "刘岳浩", 11000),
#     EmployeeModel(1004, 9007, "冯舜禹", 17000),
#     EmployeeModel(1005, 9005, "曹海欧", 15000),
#     EmployeeModel(1006, 9005, "魏鑫珑", 12000),
# ]
#
#
# # 1. 定义函数,在list_employee中查找薪资大于等于15000的所有员工
# # 2. 定义函数,在list_employee中查找部门编号是9005的所有员工
#
# # 通用
# #通用的代码，实际项目中，会放到一个单独的packge里，然后别的模块来导入packge里的模块，参照文件夹【函数式编程】
# def find(func):
#     for emp in list_employee:
#         if func(emp):
#             yield emp
#
# # 变化
# def condition01(emp):
#     return emp.money >= 15000
#
#
# def condition02(emp):
#     return emp.did == 9005
#
#

# # 变化 + 通用
# for item in find(condition01):
#     print(item.__dict__)
#
# for item in find(condition02):
#     print(item.__dict__)
#











"""
    lambda 表达式
        匿名函数:
            lambda 参数: 函数体

            def不能转换为lambda写法
                1. lambda表达式不能赋值
                2. lambda 函数体只能有一条语句

            应用:作为实参
"""

# # 写法1:有参数,有返回值
# # def func01(p1, p2):
# #     return p1 > p2
# #
# # print(func01(10, 5))
#
# func01 = lambda p1, p2: p1 > p2
# print(func01(10, 5))
#
#
#
# # 写法2:有参数,无返回值
# # def func02(p1):
# #     print("参数是:",p1)
# #
# # func02(10)
#
# func02 = lambda p1: print("参数是:", p1)
# func02(10)
#
#
#
# # 写法3:无参数,有返回值
# # def func03():
# #     return "结果"
# #
# # result = func03()
# # print(result)
#
# func03 = lambda: "结果"
# result = func03()
# print(result)
#
#
#
# # 写法4:无参数,无返回值
# # def func04():
# #     print("func04执行喽")
# #
# # func04()
#
# func04 = lambda: print("func04执行喽")
# func04()
#
#
#
#
#
#
# """
# def不能转换为lambda的写法：
# """
#
#
# def func05(p1):
#     p1[0] = 100
#
# list01 = [10]
# func05(list01)
# print(list01[0]) # 100
#
# # 1. lambda表达式不能赋值，如下
# # func05 = lambda p1:p1[0] = 100
#
#
#
#
# def func06():
#     for i in range(5):
#         print(i)
#
# func06()
#
# # 2. lambda 函数体只能有一条语句,不能如下
# # func06 = lambda :for i in range(5):print(i)
#



"""

练习

"""
# list01 = [42, 45, 5, 66, 7, 89]
#

# # 提取通用函数
# def find(func):
#     for item in list01:
#         if func(item):
#             yield item

# # 提取变化函数，
# # 实际项目中，变化函数太多了，这里是不写的，直接用lambda代替
# # def condition01(item):
# #     return item > 10
# #
# # def condition02(item):
# #     return item % 2 == 0
#

#
# # for number in find(condition02):# 向钩子上挂条件
# for number in find(lambda item: item % 2 == 0):  # lambda作为实参，代替变化函数
#     print(number)










"""
    练习1需求:
        在员工列表中,查找姓名是"刘岳浩"的员工
        在员工列表中,查找员工编号是1005的员工

    练习2需求:
        在员工列表中,查找所有员工的姓名
        在员工列表中,查找所有员工的编号和薪资

    步骤
        1. 定义函数,完成需求.
        2. 将变化点定义为函数
           将通用代码定义为函数
        3. 通用函数使用参数隔离变化点   #即def find(func):
        4. 将通用函数移动到IterableHelper类中
        5. 在当前模块中调用通用函数(lambda)
"""

# # 练习1需求:
# # 在员工列表中, 查找姓名是"刘岳浩"的员工
# # 在员工列表中, 查找员工编号是1005的员工
#
# class EmployeeModel:
#     def __init__(self, eid=0, did=0, name="", money=0.0):
#         self.eid = eid
#         self.did = did
#         self.name = name
#         self.money = money
#
#
# list_employee = [
#     EmployeeModel(1001, 9003, "林玉玲", 13000),
#     EmployeeModel(1002, 9005, "王荆轲", 16000),
#     EmployeeModel(1003, 9003, "刘岳浩", 11000),
#     EmployeeModel(1004, 9007, "冯舜禹", 17000),
#     EmployeeModel(1005, 9005, "曹海欧", 15000),
#     EmployeeModel(1006, 9005, "魏鑫珑", 12000),
# ]
#
#
# def find(func):
#     for item in list_employee:
#         if func(item):
#             yield item
#
#
# for item in find(lambda item: item.name == "刘岳浩"):
#     print(item.__dict__)
#
# for item in find(lambda item: item.eid == 1005):
#     print(item.__dict__)





# 练习2需求:
# 在员工列表中, 查找所有员工的姓名
# 在员工列表中, 查找所有员工的编号和薪资
# class EmployeeModel:
#     def __init__(self, eid=0, did=0, name="", money=0.0):
#         self.eid = eid
#         self.did = did
#         self.name = name
#         self.money = money
#
#
# list_employee = [
#     EmployeeModel(1001, 9003, "林玉玲", 13000),
#     EmployeeModel(1002, 9005, "王荆轲", 16000),
#     EmployeeModel(1003, 9003, "刘岳浩", 11000),
#     EmployeeModel(1004, 9007, "冯舜禹", 17000),
#     EmployeeModel(1005, 9005, "曹海欧", 15000),
#     EmployeeModel(1006, 9005, "魏鑫珑", 12000),
# ]
#
#
# def find(func):
#     for item in list_employee:
#         yield func(item)
#
#
# for item in find(lambda item: item.name):
#     print(item)
# for item in find(lambda item: (item.eid, item.money)):
#     print(item)


#如下是两个练习的过程
# class EmployeeModel:
#     def __init__(self, eid=0, did=0, name="", money=0.0):
#         self.eid = eid
#         self.did = did
#         self.name = name
#         self.money = money
#
#
# list_employee = [
#     EmployeeModel(1001, 9003, "林玉玲", 13000),
#     EmployeeModel(1002, 9005, "王荆轲", 16000),
#     EmployeeModel(1003, 9003, "刘岳浩", 11000),
#     EmployeeModel(1004, 9007, "冯舜禹", 17000),
#     EmployeeModel(1005, 9005, "曹海欧", 15000),
#     EmployeeModel(1006, 9005, "魏鑫珑", 12000),
# ]
#
#
# def find01():
#     for emp in list_employee:
#         if emp.name == "刘岳浩":
#             return emp
#
#
# def find02():
#     for emp in list_employee:
#         if emp.eid == 1005:
#             return emp
#
#
# def condition01(emp):
#     return emp.name == "刘岳浩"
#
#
# def condition02(emp):
#     return emp.eid == 1005
#
#
# def find(func):
#     for emp in list_employee:
#         # if emp.eid == 1005:
#         # if condition02(emp):
#         if func(emp):
#             return emp
#
#
# emp01 = IterableHelper.find_single(list_employee, lambda emp: emp.name == "刘岳浩")
# print(emp01.__dict__)
#
#
# # 2.
# def select01():
#     for emp in list_employee:
#         yield emp.name
#
# def select02():
#     for emp in list_employee:
#         yield (emp.eid, emp.money)
#
#
# def handle01(emp):
#     return emp.name
#
# def handle02(emp):
#     return  (emp.eid, emp.money)
#
# def select(func):
#     for emp in list_employee:
#         # yield (emp.eid, emp.money)
#         # yield handle02(emp)
#         yield func(emp)
#
# for item in IterableHelper.select(list_employee,lambda emp:(emp.eid, emp.money)):
#     print(item)








"""

    内置高阶函数：
        上面做的所有练习，都是可以通过内置高阶函数实现的
"""

# class EmployeeModel:
#     def __init__(self, eid=0, did=0, name="", money=0.0):
#         self.eid = eid
#         self.did = did
#         self.name = name
#         self.money = money
#
#
# list_employee = [
#     EmployeeModel(1001, 9003, "林玉玲", 13000),
#     EmployeeModel(1002, 9005, "王荆轲", 16000),
#     EmployeeModel(1003, 9003, "刘岳浩", 11000),
#     EmployeeModel(1004, 9007, "冯舜禹", 17000),
#     EmployeeModel(1005, 9005, "曹海欧", 15000),
#     EmployeeModel(1006, 9005, "魏鑫珑", 12000),
# ]
#
# # 1. map : 映射
# # map(func,iterable) -> 生成器，返回值是生成器，需要用for遍历
# #可迭代对象是个列表,映射完也是个列表，item表示可迭代对象的每个元素
# for item in map(lambda item: item.name, list_employee):
#     print(item)
#
#
# # 2.filter:过滤
# # filter(func,iterable) -> 生成器
# for item in filter(lambda emp: emp.money > 15000, list_employee):
#     print(item.__dict__)
#
#
#
# # 3.max
# # 4.min : 最大最小
# #  极值 = max(容器, key=函数)
# max_emp = max(list_employee, key=lambda item: item.money)
# print(max_emp.__dict__)
#
#
#
#
# # 5. 排序
# # -- 升序
# # 　排序结果 = sorted(容器, key=函数)
# result = sorted(list_employee, key=lambda e: e.money)
# print(result)
#
#
#
# # -- 降序
# # 　排序结果 = sorted(容器, key=函数, reverse=True)
# result = sorted(list_employee, key=lambda e: e.money, reverse=True)
# print(result)
#
#









"""
使用内置高阶函数实现：
        1. ([1,1],[2,2,2],[3,3,3],[4,4,4,4,4])
           获取元组中长度最大的列表
        2. 在员工列表列表，获取所有员工编号与姓名
        3. 在员工列表中，获取所有工资大于13000的员工
        4. 对员工列表，根据员工编号进行降序排列
        5. 获取所有工资大于15000的员工姓名.
"""
# class EmployeeModel:
#     def __init__(self, eid=0, did=0, name="", money=0.0):
#         self.eid = eid
#         self.did = did
#         self.name = name
#         self.money = money
#
#
# list_employee = [
#     EmployeeModel(1001, 9003, "林玉玲", 13000),
#     EmployeeModel(1002, 9005, "王荆轲", 16000),
#     EmployeeModel(1003, 9003, "刘岳浩", 11000),
#     EmployeeModel(1004, 9007, "冯舜禹", 17000),
#     EmployeeModel(1005, 9005, "曹海欧", 15000),
#     EmployeeModel(1006, 9005, "魏鑫珑", 12000),
# ]

# # 1.获取元组中长度最大的列表
# tuple01 = ([1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4, 4, 4])
# # lambda 参数：函数体
# # 参数得到的是容器中元素， 函数体是对元素的处理
# max_value = max(tuple01, key=lambda item: len(item))
# print(max_value)
#
# # 2.在员工列表列表，获取所有员工编号与姓名
# tuple02 = list(map(lambda emp: (emp.eid, emp.name), list_employee))
# print(tuple02)
#
# # 3.在员工列表中，获取所有工资大于13000的员工
# for item in filter(lambda element: element.money > 13000, list_employee):
#     print(item.__dict__)
#
# # 4.对员工列表，根据员工编号进行降序排列
# result = sorted(list_employee, key=lambda item: item.eid, reverse=True)
# print(result)
#
# # 5. 获取所有工资大于15000的员工姓名.
# result = list(map(lambda e: e.name, filter(lambda element: element.money > 15000, list_employee)))
# print(result)
#
