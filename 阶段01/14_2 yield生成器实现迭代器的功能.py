
"""
yield实现迭代器的功能


    迭代器 --> yield
    【迭代器的代码，不写，使用yield实现迭代器的功能，yield自动生成迭代器的代码了】

    yield 生成迭代器代码的大致规则:
        1. 将yield之前的代码定义到__next__方法中
        2. 将yield之后的数据作为__next__方法返回值

"""

# class SkillManager:
#     def __init__(self):
#         self.__skills = []
#
#     def add_skill(self, skill):
#         self.__skills.append(skill)
#
#     # def __iter__(self):
#     #     print("准备")             #类似next方法的方法体
#     #     yield self.__skills[0]   #yield有点像return，类似next方法的返回值,
#                                     #但是yield返回值后，如果在while、for循环里，不会退出循环，而是在下一次循环时，继续执行yield后面的代码
#     #
#     #     print("准备")           #第二次迭代时，从这里执行，上面的代码在上一次迭代时，已经执行过了
#     #     yield self.__skills[1]
#     #
#     #     print("准备")
#     #     yield self.__skills[2]    #最后一次，执行后，再次执行时，会自动抛异常
#
#     #上面的代码，一般写成如下，执行过程跟上面一样
#     def __iter__(self):
#         for skill in self.__skills:
#             print("准备：")
#             yield skill
#
#
#
# manager = SkillManager()
# manager.add_skill("降龙十八掌")
# manager.add_skill("六脉神剑")
# manager.add_skill("乾坤大挪移")
#
# # 迭代自定义对象
# for skill in manager:
#     print(skill)

# 开发时候，这里可以不用写，直接for循环遍历自定义对象
# iterator = manager.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)  # 降龙十八掌
#     except StopIteration:
#         break
#
# 现象:调用__iter__方法,但是不执行【因为__iter__方法里的代码，实际上都在__next__方法里】
#     调用__next__方法,执行__iter__方法
#     执行到yield返回,当再次调用__next__方法，继续执行__iter__方法剩下的代码
#





#上面一大堆代码，简化后，如下
# class SkillManager:
#     def __init__(self):
#         self.__skills = []
#
#     def add_skill(self, skill):
#         self.__skills.append(skill)
#
#     def __iter__(self):
#         for skill in self.__skills:
#             print("准备：")
#             yield skill
#
#
#
# manager = SkillManager()
# manager.add_skill("降龙十八掌")
# manager.add_skill("六脉神剑")
# manager.add_skill("乾坤大挪移")
#
# # 迭代自定义对象
# for skill in manager:
#     print(skill)






"""
练习yield

    使用yield,
    自定MyRange类
    实现range(5)效果
"""

#
# class MyRange:
#     def __init__(self, end=0):
#         self.end=end
#
#     def __iter__(self):
#         start=0
#         while start<self.end:
#             yield start  #第一次遍历时，返回0，跳到print(item)代码，第二次遍历时，才会执行下面+1的代码
#             start+=1
#
# for item in MyRange(5):
#     print(item)
#






"""
生成器：开发的时候，都是这样用
       是一种理念，循环一次 计算一次 返回一次
       是包含yield的函数

    yield --> 生成器
    
    
class Generator:        # 生成器 = 可迭代对象 + 迭代器
    def __iter__(self): # 可迭代对象
        return self
    
    def __next__(self): # 迭代器
        ....
"""

# def my_range(end):  # 不用类，直接定义函数也行
#     start = 0
#     while start < end:
#         yield start #第一次遍历时，返回0，跳到print(item)代码，第二次遍历时，才会执行下面+1的代码
#         start += 1
#
# for item in my_range(5):   #使用for来遍历,执行生成器，因为yield返回的是生成器对象
#     print(item)


#上面的for，原理还是如下代码
# range = my_range(5)     #返回生成器对象Generator()，即yield返回的是生成器对象
# iterator = range.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break








"""
练习：
    返回列表中所有数字的个位
    
    方式1:传统思想
        定义函数,循环计算目标列表里，每个元素的个位,存入列表
    方式2:生成器思想
        定义函数,循环计算每个元素的个位,通过yield返回
        
    体会:惰性操作/延迟操作/推算数据
"""
#    方式1:传统思想
# def find_number_unit(list_target):
#     list_result = []
#     for number in list_target:
#         unit = number % 10
#         list_result.append(unit)    #将结果存入列表
#     return list_result
#
# # 测试
# list01 = [54,55,36,67,28,69,90]
# result = find_number_unit(list01)
# for item in result:
#     print(item)
#
#
#



#    方式2:生成器思想
# def find_number_unit(list_target):
#     for number in list_target:
#         unit = number % 10
#         yield unit                      #返回推算出的结果，然后执行下面的print(item)，没有将结果存入列表
#
# # 测试
# list01 = [54,55,36,67,28,69,90]
#
# result = find_number_unit(list01)   #给函数传递参数
# for item in result:                 #使用for来遍历,执行生成器，因为yield返回的是生成器对象
#     print(item)
#
#
#






"""
通过容器执行生成器
    一般都是通过for执行
"""
# def find_number_unit(list_target):
#     for number in list_target:
#         unit = number % 10
#         yield unit                      #返回推算出的结果，然后执行下面的print(item)，没有将结果存入列表
#
# # 测试
# list01 = [54,55,36,67,28,69,90]

# result = find_number_unit(list01)   #给函数传递参数
# for item in result:                 #使用for来遍历,执行生成器，因为yield返回的是生成器对象
#     print(item)
#


# 生成器缺点1:
# 只能用一次，因为最后会抛异常，除非再创建一次生成器对象result = find_number_unit(list01) ，如下
# result = find_number_unit(list01)
# for item in result:
#     print(item)
#
# result = find_number_unit(list01)
# for item in result:
#     print(item)



# 生成器缺点2:不能使用索引/切片
# result[-1]



# 可以通过容器执行生成器
# 但是一般都是用for执行
# 缺点:将所有数据加载到内存中,占用可能过多.
# 但是容器里的数据，可以多次使用了，如下，并且可以使用索引切片
# result = tuple(find_number_unit(list01))
#
# for item in result:
#     print(item)
#
# for item in result:
#     print(item)
#




"""
    函数返回结果:
        return 数据  -- 单个数据
        yield 数据   -- 多个数据【大于1个】
"""
# class EmployeeModel:
#     def __init__(self, eid=0, did=0, name="", money=0.0):
#         self.eid = eid  #员工编号
#         self.did = did  #部门编号
#         self.name = name
#         self.money = money
#
# list_employee = [
#     EmployeeModel(1001, 9003, "林玉玲", 13000),
#     EmployeeModel(1002, 9003, "王荆轲", 16000),
#     EmployeeModel(1003, 9003, "刘岳浩", 11000),
#     EmployeeModel(1004, 9003, "冯舜禹", 17000),
#     EmployeeModel(1005, 9003, "曹海欧", 15000),
#     EmployeeModel(1006, 9003, "魏鑫珑", 12000),
# ]

# # 1. 定义函数,在list_employee中查找薪资大于等于15000的所有员工
# def find_employees_gt_15k():
#     for emp in list_employee:
#         if emp.money >= 15000:
#             yield emp
# for item in find_employees_gt_15k():
#     print(item.__dict__)




# # 2. 定义函数,在list_employee中查找员工编号为1005的员工

# def find_employee_at_eid():
#     for emp in list_employee:
#         if emp.eid == 1005:
#             return emp     #由于找的是单个员工，不是大于一个的多个，
                             #所以用return返回对象，而不是yield返回生成器，所以后面也不用for遍历，而是直接print对象
# employee = find_employee_at_eid()
# print(employee.__dict__)
#



# # 3. 定义函数,在list_employee中查找所有员工的姓名
# def find (targerlist):
#     for item in targerlist:
#             yield item.name
#
# for item in find(list_employee):
#     print(item)
#



# # 4. 定义函数,在list_employee中查找薪资最高的员工
# def get_max_employee_by_money():
#     max_emp = list_employee[0]
#     for i in range(1,len(list_employee)):
#         if max_emp.money  < list_employee[i].money:
#             max_emp = list_employee[i]
#     return max_emp
#
# emp = get_max_employee_by_money()
# print(emp.__dict__)
#



