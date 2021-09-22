"""
练习

"""
# 1. 定义函数,在list_employee中查找薪资大于等于15000的所有员工
# 2. 定义函数,在list_employee中查找部门编号是9005的所有员工

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


# # 变化
# def condition01(emp):
#     return emp.money >= 15000
#
#
# def condition02(emp):
#     return emp.did == 9005
#
#
#
# #导入通用
# from common.common import IterableHelper
#
#
#
# # 变化 + 通用
# #将被查询的列表或者可迭代对象，以及查询条件函数【只是函数名，不要加小括号，因为是将函数作为参数传递，不是调用执行函数】，
# # 作为参数，给通用代码
# for item in IterableHelper.find(list_employee,condition01):
#     print(item.__dict__)
#
# for item in IterableHelper.find(list_employee,condition02):
#     print(item.__dict__)
#




#
# # # 如下不写，使用lambda代替变化条件，实际项目当中，都是使用lambda代替变化条件的
# # def condition01(emp):
# #     return emp.money >= 15000
# #
# #
# # def condition02(emp):
# #     return emp.did == 9005
# #
#
#
# #导入通用
# from common.common import IterableHelper
#
# # 变化 + 通用
# for item in IterableHelper.find(list_employee, lambda item: item.money >= 15000):
#     print(item.__dict__)
#
# for item in IterableHelper.find(list_employee, lambda item: item.did == 9005):
#     print(item.__dict__)











"""
练习

    步骤
        1. 定义函数,完成需求.
        2. 将通用代码定义为函数
            将变化点定义为函数
        3. 通用函数使用参数隔离变化点
        4. 在IterableHelper类中创建通用函数
        5. 在当前模块中调用通用函数(lambda)
"""

from common.common import IterableHelper


class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0.0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money


list_employee = [
    EmployeeModel(1001, 9003, "林玉玲", 13000),
    EmployeeModel(1002, 9005, "王荆轲", 16000),
    EmployeeModel(1003, 9003, "刘岳浩", 11000),
    EmployeeModel(1004, 9007, "冯舜禹", 17000),
    EmployeeModel(1005, 9005, "曹海欧", 15000),
    EmployeeModel(1006, 9005, "魏鑫珑", 12000),
]

"""
    练习1需求:
        在员工列表中,查找删除薪资15000以内的所有员工
        在员工列表中,查找删除部门编号是9005的所有员工
"""
#
# # 1. 定义函数,完成需求.
# def delete01(list_target):
#     for i in range(len(list_target) - 1, -1, -1):
#         if list_target[i].money < 15000:
#             del list_target[i]
#
#
# def delete02(list_target):
#     for i in range(len(list_target) - 1, -1, -1):
#         if list_target[i].did == 9005:
#             del list_target[i]
#
#
# # 2. 将通用代码定义为函数
# #     将变化点定义为函数
# def delete(list_targe, func):  # 3. 通用函数使用参数隔离变化点
#     for i in range(len(list_targe) - 1, -1, -1):
#         if func(list_targe[i]): #list_targe[i]作为参数传给condition01 02
#             del list_targe[i]
#
#
# def condition01(emp):
#     return emp.money < 15000
#
# def condition02(emp):
#     return emp.did == 9005
#
#
# # 5、在当前模块中调用通用函数(lambda)，lambda写法类似condition
# IterableHelper.delete(list_employee, lambda emp: emp.money < 15000)
# IterableHelper.delete(list_employee, lambda emp: emp.did == 9005)
#
# for item in list_employee:
#     print(item.__dict__)






"""
    练习2需求:
        在员工列表中,查找薪资最高的员工
        在员工列表中,查找员工编号最大的员工

"""
#
# ## # 1. 定义函数,完成需求.
# def max_wages(list_target):
#     max = list_target[0]
#     for i in range(1, len(list_target)):
#         if max.money < list_target[i].money:
#             max = list_target[i]
#     return max
#
#
# def max_eid(list_target):
#     max = list_target[0]
#     for i in range(1, len(list_target)):
#         if max.eid < list_target[i].eid:    #这两段代码，if语句里的小于号是一样的，只是一个比较money，一个比较eid
#             max = list_target[i]
#     return max
#
#
# # # 2. 将通用代码定义为函数
# # #     将变化点定义为函数
# def max(list_target, func):  # 3. 通用函数使用参数隔离变化点
#     max = list_target[0]
#     for i in range(1, len(list_target)):
#         if func(max) < func(list_target[i]):  # list_target[i],max作为参数传给condition01 02
#             max = list_target[i]
#     return max
#
#
# def condition01(item):
#     return item.money
#
#
# def condition02(item):
#     return item.eid


# # # 5、在当前模块中调用通用函数(lambda)，lambda写法类似condition
# result01 = IterableHelper.max(list_employee, lambda emp: emp.money)
# print(result01.__dict__)
# result02 = IterableHelper.max(list_employee, lambda emp: emp.eid)
# print(result02.__dict__)
#
#



"""
    练习3需求:
        在员工列表中,根据薪资升序排列
        在员工列表中,根据员工编号升序排列

"""

def wages_ascending_order(list_target):
    for i in range(len(list_target) - 1):
        for c in range(i + 1, len(list_target)):
            if list_target[i].money > list_target[c].money:
                list_target[i], list_target[c] = list_target[c], list_target[i]

def eid_ascending_order(list_target):
    for i in range(len(list_target) - 1):
        for c in range(i + 1, len(list_target)):
            if list_target[i].eid > list_target[c].eid:
                list_target[i], list_target[c] = list_target[c], list_target[i]


def ascending_order(list_target,func):
    for i in range(len(list_target) - 1):
        for c in range(i + 1, len(list_target)):
            if func(list_target[i]) > func(list_target[c]):
                list_target[i], list_target[c] = list_target[c], list_target[i]

def condition01(item):
    return item.money

def condition01(item):
    return item.eid


IterableHelper.ascending_order(list_employee, lambda item: item.money)
for item in list_employee:
    print(item.money)


IterableHelper.ascending_order(list_employee, lambda item: item.eid)
for item in list_employee:
    print(item.eid)



