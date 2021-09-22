"""
    内置生成器
            enumerate()，得到索引

"""

#list01 = [54, 5, 6, 76, 8, 9]

# 遍历元素 -- 读取
# for item in list01:
#     print(item)


# 不能如下写，因为修改的是变量item，而不是列表
# for item in list01:
#     item=0


# 遍历索引 -- 修改，所有元素变为0
# 这是通过索引，遍历元素
# for i in range(len(list01)):
#     list01[i] = 0


# 内置生成器enumerate(),
# 如下，得到的结果是多个元组，元组的内容是列表的(索引, 元素)
# for item in enumerate(list01):
#     print(item)

#一般如下写，元组拆包
#奇数变为0
# for i, element in enumerate(list01):
#     if element % 2:
#         list01[i] = 0
# print(list01)
#






"""
    练习1: 创建字典,遍历字典,打印索引/键/值
    练习2: 创建列表,将列表中大于10的数字,设置为0
"""
# dict01 = {"a": "A", "b": "B"}
# # for item in enumerate(dict01.items()):  得到的是 (0, ('a', 'A'))
# for i, (k, v) in enumerate(dict01.items()):
#     print(i, k, v)
#



# list01 = [5, 6, 67, 8, 9, 9, 65, 43, 7]
# for i, item in enumerate(list01):
#     if item > 10:
#         list01[i] = 0
#
# print(list01)
#




"""
内置生成器 
    zip:
        将多个列表，竖着取值，合成元组
    如下，得到
    ('1', '2', '3', '4')
    ('5', '6', '7', '8')
    ('9', '10', '11', '12')

"""
# list01 = ["1", "5", "9"]
# list02 = ["2", "6", "10"]
# list03 = ["3", "7", "11"]
# list04 = ["4", "8", "12"]
#
# for item in zip(list01, list02,list03,list04):
#     print(item)
#



# # 练习:通过zip实现矩阵转置
# list01 = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
# ]
# #固定行
# for item in zip(list01[0],list01[1],list01[2],list01[3]):
#     print(item)
#
# #或使用*号将列表元素拆开
# for item in zip(*list01):
#     print(item)
#
#
# list02 = []
# for item in zip(*list01):
#      list02.append(list(item))
# print(list02)








"""
    生成器函数【包含yield的函数，被别人调用】
        给其他人用
        
    生成器表达式
        给自己使用

"""

# list01 = [54, 65.5, True, "a", False, "b", 3, "c"]

# 查找所有字符串
# list_result = []
# for item in list01:
#     if type(item) == str:
#         list_result.append(item)
# print(list_result)

# # 列表推导式
##上面的代码，可以用列表推导式，简写如下
# list_result = [item for item in list01 if type(item) == str]
# for item in list_result:
#     print(item)

# 生成器表达式
#只需要把列表推导式里，列表的【】，写成（）就行，此时得到的是生成器对象，需要使用for循环执行
#程序执行过程，也是循环一次 计算一次 返回一次的过程
# list_result = (item for item in list01 if type(item) == str)
# for item in list_result:
#     print(item)
#




"""
练习
# 要求：使用列表推导式，生成器表达式完成.
# 通过调试，体会差异.
"""
# list01 = [54, 65.5, True, "a", False, "b", 3, "c"]
#
# # 练习:在列表中获取所有大于10的小数的平方.
# list03 = [item ** 2 for item in list01 if type(item) == float and item > 10]
# for number in list03:
#     print(number)
#
# generator03 = (item ** 2 for item in list01 if type(item) == float and item > 10)
# for number in generator03:
#     print(number)





"""
    将生成器函数,改写为生成器表达式
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
#     EmployeeModel(1002, 9003, "王荆轲", 16000),
#     EmployeeModel(1003, 9003, "刘岳浩", 11000),
#     EmployeeModel(1004, 9003, "冯舜禹", 17000),
#     EmployeeModel(1005, 9003, "曹海欧", 15000),
#     EmployeeModel(1006, 9003, "魏鑫珑", 12000),
# ]

# # 1. 在list_employee中查找薪资大于等于15000的所有员工
# employees_gt_15k = (emp for emp in list_employee if emp.money >= 15000)
# for item in employees_gt_15k:
#     print(item.__dict__)
#
# # 3. 在list_employee中查找所有员工的姓名
# names_by_employee = (emp.name for emp in list_employee)
# for name in names_by_employee:
#     print(name)
#







