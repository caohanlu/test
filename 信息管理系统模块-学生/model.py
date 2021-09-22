class StudentModel:
    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        self.sid = sid  # 学生编号：对数据进行唯一标识(全球唯一标识符)   # 自增长1001   1002   1003

    # 对属性，即实例变量score进行有效性验证
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if value < 0:
            value = 0
        elif value > 100:
            value = 100
        self.__score = value