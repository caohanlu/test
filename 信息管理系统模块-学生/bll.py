class StudentController:
    def __init__(self):
        self.__list_students = []
        self.__start_sid = 1001

    # 只读属性
    @property
    def list_students(self):
        return self.__list_students

    def add_student(self, stu):
        """
            添加学生
        :param stu: 需要添加的学生对象
        """
        stu.sid = self.__start_sid
        self.__start_sid += 1
        self.__list_students.append(stu)

    def remove_student(self, sid):
        """
            删除学生
        :param sid: int类型的学生编号
        :return: bool类型,是否删除成功
        """
        for student in self.__list_students:
            if student.sid == sid:
                self.__list_students.remove(student)
                return True  # 删除成功
        return False  # 删除失败

