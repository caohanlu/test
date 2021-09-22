
"""
    迭代 iter:每一次对过程的重复称为一次“迭代”，
             而每一次迭代得到的结果会作为下一次迭代的初始值。

        可迭代对象iterable:能够完成迭代过程的对象,例如字符串，需要被迭代或者for循环遍历的类，即具有__iter__()函数

        迭代器iterator:实施迭代过程的类的对象iterator，即具有__next__()函数的类


"""

# message = "我是齐天大圣孙悟空"


# for item in message:
#     print(item)


# for 循环原理,
# 下面的代码，跟上面的两行代码，是一样的
# iterator = message.__iter__()   # 1. 获取迭代器这个类的对象
# while True:
#     try:
#         item = iterator.__next__()  # 2. 获取下一个元素
#         print(item)
#     except StopIteration:   # 3. 如果没有元素,则停止循环.    for检测的错误类型是StopIteration，遍历完成后退出循环
#         break


# 面试题:可以参与for循环的条件是?
# 能够获取迭代器对象(可迭代对象)，即具有__iter__函数


"""

练习1:使用迭代思想，打印元组中所有元素。

练习2:不使用for循环，打印字典中所有记录(键和值)

    都是使用迭代器

"""
# tuple01 = (43, 4, 5, 67, 87, 89)
#
# iterator = tuple01.__iter__()
#
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break


# dict01 = {"a": "A", "b": "B"}
#
# iterator = dict01.__iter__()
#
# while True:
#     try:
#         key = iterator.__next__()   #对于字典，迭代器获取的元素是字典的key
#         value = dict01[key]
#         print(key, value)
#     except StopIteration:
#         break
#


"""
    让自定义对象参与for循环
    即迭代自定义对象
"""

#
# class SkillIterator:                  #迭代器类
#     def __init__(self, data):
#         self.data = data
#         self.index = -1
#
#     def __next__(self):
#         self.index += 1                     #__next__函数被调用一次，索引就增加一次
#         if self.index < len(self.data):
#             return self.data[self.index]
#         else:
#             raise StopIteration()         #for循环内部，检测的是StopIteration() 异常
#
#
# class SkillManager:                     #技能管理类，即需要被迭代的类
#     def __init__(self):
#         self.__skills = []
#
#     def add_skill(self, skill):
#         self.__skills.append(skill)
#
#     def __iter__(self):  #由于可迭代对象需要具有__iter__()函数，并且返回一个迭代器类的对象，所以定义该函数
#         return SkillIterator(self.__skills)  #由于迭代器需要具有__next__()函数，所以创建迭代器类的对象，
#                                              #这个类有__next__()函数函数.并且把列表作为参数，传给迭代器类的构造函数
#
#
# manager = SkillManager()
# manager.add_skill("降龙十八掌")
# manager.add_skill("六脉神剑")
# manager.add_skill("乾坤大挪移")
#
#
# #创建__iter__()，__next__()函数后,下面这段代码可以直接注释掉了，直接for循环遍历自定义对象就行
##for的本质，就类似如下代码
# # iterator = manager.__iter__()
# # while True:
# #     try:
# #         item = iterator.__next__()
# #         print(item)  # 降龙十八掌
# #     except StopIteration:
# #         break
# #
# # 创建__iter__()，__next__()函数后，直接for可以迭代自定义对象，即自己创建的类的对象
# for skill in manager:
#     print(skill)


"""
练习
    迭代员工管理器
"""

#
# class EmployeeIterator:
#     def __init__(self, list):
#         self.list = list
#         self.index = -1
#
#     def __next__(self):
#         self.index += 1
#         if self.index < len(self.list):
#             return self.list[self.index]
#         else:
#             raise StopIteration()
#
#
# class EmployeeManager:
#     def __init__(self):
#         self.all_employee = []
#
#     def add_employee(self, emp):
#         self.all_employee.append(emp)
#
#     def __iter__(self):
#         return EmployeeIterator(self.all_employee)
#
#
# manager = EmployeeManager()
#
# manager.add_employee("老王")
# manager.add_employee("老李")
# manager.add_employee("老孙")
#
# # iterator=manager.__iter__()
# # while True:
# #     try:
# #         item=iterator.__next__()
# #         print(item)
# #     except StopIteration:
# #         break
#
# #可直接for循环遍历自定义对象了
# for item in manager:
#     print(item)


"""
    自定MyRange类
    实现range(5)效果
"""
# class MyRangeIterator:
#     def __init__(self, end=0):
#         self.end=end
#         self.index=-1
#     def __next__(self):
#         self.index+=1
#         if self.index < self.end:
#             return self.index
#         else:
#             raise StopIteration()
#
# class MyRange:
#     def __init__(self, end=0):
#         self.end=end
#     def __iter__(self):
#         return MyRangeIterator(self.end)
#
# #for循环本质如下，写好iter和next函数后，这部分代码可以删掉，直接for语句遍历自定义对象就行
# # myrange=MyRange(5)
# # iterator=myrange.__iter__()
# # while True:
# #     try:
# #         item=iterator.__next__()
# #         print(item)
# #     except StopIteration:
# #         break
#
#
#
#
# for item in MyRange(5):
#     print(item)
#
#
#
# # 可以生成撑爆内存的数字
# # 循环一次  计算一次  返回一次，
# # 返回后的数据就消失了，没有存在内存里
# for item in MyRange(9999999999999999999999999999999):
#     print(item)
#
# for item in range(9999999999999999999999999999999):
#     print(item)
#



