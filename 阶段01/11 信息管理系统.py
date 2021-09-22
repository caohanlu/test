"""
    信息管理系统：

    基本的操作：增删改查

    分配职责：
        数据模型类Model：定义需要处理的数据类型。比如学生信息类，商品信息类，疫情信息类。
        界面视图类View：负责处理界面逻辑，比如显示菜单，获取输入，显示结果等。
        逻辑控制类Controller：负责存储学生信息，处理业务逻辑。比如添加、删除等
        入口main：项目启动运行

"""




"""
    基本调用
"""

# class XXView:
#     def __init__(self):
#         self.controller = XXController()
#
#     def func01(self):
#         self.controller.func02()
#
# class XXController:
#     def func02(self):
#         print("func02执行喽")
#
# view = XXView()# 内部创建Controller
# view.func01() # 内部调用func02
#




"""
    学生信息管理系统，基于MVC架构
"""

#
# # 2.数据模型【学生类】
# class StudentModel:
#     def __init__(self, name="", age=0, score=0, sid=0):
#         self.name = name
#         self.age = age
#         self.score = score
#         self.sid = sid  # 学生编号：对数据进行唯一标识(全球唯一标识符)   # 自增长1001   1002   1003
#
#     # 对属性，即实例变量score进行有效性验证
#     @property
#     def score(self):
#         return self.__score
#
#     @score.setter
#     def score(self, value):
#         if value < 0:
#             value = 0
#         elif value > 100:
#             value = 100
#         self.__score = value
#
#
#
# # 3.界面逻辑，负责处理界面逻辑
# class StudentView:
#
#     def __init__(self):
#         self.__controller = StudentController()
#
#     def __display_menu(self):
#         print("1) 添加学生信息")
#         print("2) 显示学生信息")
#         print("3) 删除学生信息")
#         # ...
#
#     def __select_menu(self):
#         item = input("请输入选项：")
#         if item == "1":
#             self.__input_student() # 先写调用,再快捷键生成定义函数代码  # atl + 回车
#         elif item == "2":
#             self.__show_students()
#         elif item == "3":
#             self.__delete_student()
#
#     def main(self):
#         """
#             入口函数，把别的函数都做成私有函数，然后在入口函数里，调用私有函数，实例对象通过入口函数，来调用这些私有函数
#         """
#         while True:
#             self.__display_menu()
#             self.__select_menu()
#
#     def __input_student(self):
#         stu = StudentModel()
#         stu.name = input("请输入学生姓名：")
#         stu.age = int(input("请输入学生年龄："))
#         stu.score = int(input("请输入学生成绩："))
#         self.__controller.add_student(stu)
#
#     def __show_students(self):
#         for stu in self.__controller.list_students:
#             print(f"{stu.name}的编号是{stu.sid}年龄是{stu.age}成绩是{stu.score}")
#
#     def __delete_student(self):
#         sid = int(input("请输入需要删除的学生编号："))
#         if self.__controller.remove_student(sid):
#             print("删除成功")
#         else:
#             print("删除失败")
#
#
# # 4.业务逻辑
# class StudentController:
#     def __init__(self):
#         self.__list_students = []
#         self.__start_sid = 1001
#
#     # 只读属性
#     @property
#     def list_students(self):
#         return self.__list_students
#
#     def add_student(self, stu):
#         """
#             添加学生
#         :param stu: 需要添加的学生对象
#         """
#         stu.sid = self.__start_sid
#         self.__start_sid += 1
#         self.__list_students.append(stu)
#
#     def remove_student(self, sid):
#         """
#             删除学生
#         :param sid: int类型的学生编号
#         :return: bool类型,是否删除成功
#         """
#         for student in self.__list_students:
#             if student.sid == sid:
#                 self.__list_students.remove(student)
#                 return True  # 删除成功
#         return False  # 删除失败
#
#
# # 1.入口
# view = StudentView()
# view.main()









"""
    参照student_info_manager.py完成商品管理信息系统
    
    1. 实现添加商品信息功能
        View -- 录入商品信息
        Controller -- 添加商品信息
    2. 实现显示所有商品信息功能
    3. 实现删除商品信息功能
"""
#
# class CommodityView:
#     def __init__(self):
#         self.__controller = CommodityController()
#
#     def __display_menu(self):
#         print("1) 添加商品信息")
#         print("2) 显示商品信息")
#         print("3) 删除商品信息")
#
#     def __select_menu(self):
#         item = input("请输入选项：")
#         if item == "1":
#             self.__input_commodity()
#         elif item == "2":
#             self.__show_commodity()
#         elif item == "3":
#             self.__delete_commodity()
#
#     def main(self):
#         """
#             入口函数
#         """
#         while True:
#             self.__display_menu()
#             self.__select_menu()
#
#     def __input_commodity(self):
#         commodity = CommodityModel()
#         commodity.name = input("请输入商品名称：")
#         commodity.price = float(input("请输入商品单价："))
#         self.__controller.add_commodity(commodity)
#
#     def __show_commodity(self):
#         for commodity in self.__controller.list_commoditys:
#             print("%s商品编号是%d,单价是%.2f" % (commodity.name, commodity.cid, commodity.price))
#
#     def __delete_commodity(self):
#         cid = int(input("请输入商品编号："))
#         if self.__controller.remove_commodity(cid):
#             print("删除成功")
#         else:
#             print("删除失败")
#
#
# class CommodityController:
#     def __init__(self):
#         self.__list_commoditys = []
#         self.__start_cid = 1001
#
#     @property
#     def list_commoditys(self):
#         return self.__list_commoditys
#
#     def add_commodity(self, commodity):
#         commodity.cid = self.__start_cid
#         self.__start_cid += 1
#         self.__list_commoditys.append(commodity)
#
#     def remove_commodity(self, cid):
#         for commodity in self.__list_commoditys:
#             if commodity.cid == cid:
#                 self.__list_commoditys.remove(commodity)
#                 return True
#         return False
#
#
# view = CommodityView()
# view.main()
#




"""
员工管理系统
    增删改查
"""

#
# class EmployeeModel:
#     def __init__(self, eid=0, did=0, name="", money=0.0):
#         self.eid = eid
#         self.did = did
#         self.name = name
#         self.money = money
#
#
# class EmployeeView:
#     def __init__(self):
#         self.__controller = EmployeeController()
#
#     def __display_menu(self):
#         print("1) 添加员工信息")
#         print("2) 显示员工信息")
#         print("3) 删除员工信息")
#         print("4) 修改员工信息")
#
#     def __select_menu(self):
#         item = input("请输入选项：")
#         if item == "1":
#             self.__input_employee()
#         elif item == "2":
#             self.__show_employee()
#         elif item == "3":
#             self.__delete_employee()
#         elif item == "4":
#             self.__modify_employee()
#
#     def main(self):
#         """
#             入口函数
#         """
#         while True:
#             self.__display_menu()
#             self.__select_menu()
#
#     def __input_employee(self):
#         employee = EmployeeModel()
#         employee.name = input("请输入员工姓名：")
#         employee.did = int(input("请输入部门编号："))
#         employee.money = int(input("请输入员工薪资："))
#         # self.__controller.add_employee(employee)
#
#     def __show_employee(self):
#         for employee in self.__controller.list_employees:
#             print("%s的员工编号是%d,部门编号是%d,工资是%.2f" % (employee.name, employee.eid, employee.did, employee.money))
#
#     def __delete_employee(self):
#         cid = int(input("请输入商品编号："))
#         if self.__controller.remove_employee(cid):
#             print("删除成功")
#         else:
#             print("删除失败")
#
#     def __modify_employee(self):
#         employee = EmployeeModel()
#         employee.eid = int(input("请输入需要修改的员工编号："))
#         employee.name = input("请输入修改后的员工姓名：")
#         employee.did = int(input("请输入修改后的部门编号："))
#         employee.money = int(input("请输入修改后的员工薪资："))
#
#         if self.__controller.update_employee(employee):
#             print("修改成功")
#         else:
#             print("修改失败")
#
#
# class EmployeeController:
#     def __init__(self):
#         self.__list_employees = []
#         self.__start_eid = 1001
#
#     @property
#     def list_employees(self):
#         return self.__list_employees
#
#     # typing 类型标注
#     def add_employee(self, employee:EmployeeModel):#employee:EmployeeModel表示参数是EmployeeModel类的对象，这样参数就可以点出提示信息
#         employee.eid = self.__start_eid
#         self.__start_eid += 1
#         self.__list_employees.append(employee)
#
#     def remove_employee(self, cid):
#         for commodity in self.__list_employees:
#             if commodity.cid == cid:
#                 self.__list_employees.remove(commodity)
#                 return True
#         return False
#
#     def update_employee(self, employee):
#         for item in self.__list_employees:
#             if item.eid == employee.eid:
#                 item.did = employee.did
#                 item.name = employee.name
#                 item.money = employee.money
#                 return True
#         return False
#
#
# view = EmployeeView()
# view.main()

