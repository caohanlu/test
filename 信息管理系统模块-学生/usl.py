from  bll import StudentController
from  model import StudentModel


class StudentView:

    def get_number(self, message):
        while True:
            try:
                number = int(input(message))
                return number
            except:
                print("输入错误")

    def __input_student(self):
        stu = StudentModel()
        stu.name = input("请输入学生姓名：")
        # stu.age = int(input("请输入学生年龄："))
        # stu.score = int(input("请输入学生成绩："))
        stu.age = self.get_number("请输入学生年龄：")
        stu.score = self.get_number("请输入学生成绩：")
        self.__controller.add_student(stu)

    def __init__(self):
        self.__controller = StudentController()

    def __display_menu(self):
        print("1) 添加学生信息")
        print("2) 显示学生信息")
        print("3) 删除学生信息")
        # ...

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            self.__input_student()  # 先写调用,再快捷键生成定义函数代码  # atl + 回车
        elif item == "2":
            self.__show_students()
        elif item == "3":
            self.__delete_student()

    def main(self):
        """
            入口函数，把别的函数都做成私有函数，然后在入口函数里，调用私有函数，实例对象通过入口函数，来调用这些私有函数
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __show_students(self):
        for stu in self.__controller.list_students:
            print(f"{stu.name}的编号是{stu.sid}年龄是{stu.age}成绩是{stu.score}")

    def __delete_student(self):
        sid = int(input("请输入需要删除的学生编号："))
        if self.__controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")

