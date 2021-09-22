"""
    异常处理

        程序异常时，会转到函数的调用语句，并且函数的调用语句的后续代码不再执行

        异常处理的目的:让后续代码继续执行
                    错误状态(向上翻)  -->   正常状态(向下走)

        核心价值：保障程序按照既定流程执行
"""


# def div_apple(apple_count):
#     person_count = int(input("请输入人数:"))
#     result = apple_count / person_count
#     print("每人%d个苹果" % (result))
#


# 写法1:对症下药(官方建议)
# try:                    # 检测可能出错的代码
#     div_apple(10)

# except ValueError:      # 定位错误代码，不同的错误，错误代码是不一样的，程序报错时会有报错代码
#     print("不能输入非整数类型")
# except ZeroDivisionError:
#     print("不能输入零")
#
#
# print("后续逻辑")         #出错后，后续这个代码也可正常执行
#





# 写法2:包治百病(常用)
# try:                # 检测可能出错的代码
#     div_apple(10)
#
# except:             # 定位全部错误代码，也可以这样写except Exception:
#     print("出错喽")
#
# print("后续逻辑")
#





# 写法3:一定执行的逻辑
# try:                # 检测可能出错的代码
#     div_apple(10)
#     # 例如 打开文件
#     # 处理文件(错误)
#
# finally:            # 最终 无论是否发生错误,一定执行的代码.
#     print("分苹果结束")
#     # 关闭文件
#
# print("后续逻辑")






# 写法4:没有出错才执行的逻辑
# try:                # 检测可能出错的代码
#     div_apple(10)
# except:
#     print("出错啦")
# else:               # 没有出错才执行的逻辑
#     print("分苹果成功啦")
#
# print("后续逻辑")
#





"""
练习
    定义函数,获取成绩
    如果成绩输入有误,循环录入,直到正确为止.
"""
# def get_score():
#     while True:
#         try:
#             score = float(input("请输入成绩:"))
#             return score  # 退出函数，退出循环
#         except:
#             print("成绩输入有误!")
#
#
# print(get_score())  # 有效的成绩
#
#





"""

    练习:对员工管理器进行异常处理
    
    def __input_student(self):
    函数获取了好几次学生信息，每次输入都有可能出错，可以抽象成一个函数，并且进行try
    只针对年龄和成绩，因为都是int整数类型
    如下


"""

# def get_number(self, message):
#     while True:
#         try:
#             number = int(input(message))
#             return number
#         except:
#             print("输入错误")
#
#
# def __input_student(self):
#     stu = StudentModel()
#     stu.name = input("请输入学生姓名：")
#     stu.age = self.get_number("请输入学生年龄：")
#     stu.score = self.get_number("请输入学生成绩：")
#     self.__controller.add_student(stu)







"""
    raise
    
    主动抛出异常(快速传递错误消息)
    用的不多
"""
#
#
# class Wife:
#     def __init__(self, age=0):
#         self.age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if 22 <= value <= 30:
#             self.__age = value
#         else:
#             raise Exception("年龄超过范围","还可以","写很多","是个元组")    # 主动抛出异常(快速传递错误消息)
#
# try:
#     w01 = Wife(300)
#     print(w01.age)
# except Exception as e: # 通过e变量操作抛出的异常对象
#     print(e.args)      #获取元组元素
#     print("出错啦")
#






