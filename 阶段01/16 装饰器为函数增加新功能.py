
"""
    函数作用域
        - 外部嵌套作用域 语法
         # 内部函数可以访问外部函数变量
         # 如果修改外部函数变量,必须通过nonlocal声明
"""
# # 外部函数
# def func01():
#     a = 10         #局部变量：对文件而言    #外部嵌套变量：对func02而言
#
#     def func02(): # 内部函数
#         print(a)  # 内部函数可以访问外部函数变量
#
#     func02()      #加这句代码，则执行func01时，才会执行内部函数func02
#
#
#
# # 调用外部函数(内部函数func02不执行)
# func01()
#





#
#
# def func03():  # 外部函数
#     a = 10
#
#     def func04():  # 内部函数
#         nonlocal a  # 如果修改外部函数变量,必须通过nonlocal声明
#         a = 20
#
#     func04()
#
#     print(a)# ? 20
#
#
# func03()








"""
    闭包 - 
        语法：外面一个函数，里面一个函数，里面函数使用外面函数的变量，外面函数返回值是里面函数
        字面意思：封闭内存空间(即在外部函数执行完后，保存外部函数的栈帧，正常来讲，外部函数执行完后，栈帧就会被释放)
        目的：内部函数,可以在外部函数执行后,访问其变量
        
"""

#
# def func01():
#     a = 10
#
#     def func02():
#         print(a)
#
#     return func02  #返回值是内部函数的函数名内存地址，而不是执行内部函数，所以不需要加小括号（）
#
#
# result = func01()  # 调用外部函数(不执行内部函数)
# result()# 10       # 通过外部函数的返回值调用内部函数，可以访问外部变量，是因为外部函数栈帧没释放
#
#





"""
    闭包 - 应用
        逻辑连续【：但是python中，一般都是使用面向对象的方式，实现这个功能】
            外部函数调用一次,内部函数调用多次,
            内部函数都可以访问外部函数变量

            从一次得钱,到多次花钱的过程,可以连续不中断，如下
                得到了1000元压岁钱
                购买了变形金刚,花了200元,还剩下800元
                购买了遥控飞机,花了500元,还剩下300元
                购买了糖,花了100元,还剩下200元

"""


# def give_gife_money(money):  # 得钱
#     print("得到了%d元压岁钱" % money)
#
#     def child_buy(commodity, price):  # 花钱
#         nonlocal money
#         money -= price
#         print("购买了%s,花了%d元,还剩下%d元" % (commodity, price, money))
#
#     return child_buy
#
# action = give_gife_money(1000)   #调用外部函数，得到钱
# action("变形金刚",200)            #通过外部函数的返回值，调用内部函数，花钱，如下，内部函数调用了多次，修改了多次外部函数的变量
# action("遥控飞机",500)
# action("糖",100)
#
#




"""
    装饰器 ：
    就是闭包的应用
    可以实现不改变旧函数func01的调用,以及内部代码的情况下
    为其增加新功能(下面例子的新功能，是打印旧函数名称)】
"""

#如下就是装饰器的语法框架
# def print_func_name(func):                      #旧功能作为参数，传进来
#     def wrapper(*args, **kwargs):
#         print("-----", func.__name__, "-----")  # 执行新功能：打印传入的函数名称
#         return func(*args, **kwargs)            # 执行旧功能：执行传入的函数，并且返回传入的函数的返回值
#     return wrapper
#
#
# # func01是旧功能，装饰器是增加的新功能
# def func01():
#     print("func01执行了")
#
#
# # 调用外部函数print_func_name，外部函数的返回值是内部函数wrapper，把内部函数wrapper内存地址，赋值给func01
# func01 = print_func_name(func01)
# # 调用内部函数wrapper
# func01()
#





# #原理就是如上，但是实际开发如下写
# def print_func_name(func):                      #旧功能作为参数，传进来
#     def wrapper(*args, **kwargs):
#         print("-----", func.__name__, "-----")  # 执行新功能：打印传入的函数名称
#         return func(*args, **kwargs)            # 执行旧功能：执行传入的函数，因为带了小括号（），并且返回旧功能的返回值
#     return wrapper
#
#
# @print_func_name
# def func01():
#     print("func01执行了")
#











"""
    练习:使用装饰器，为旧功能增加新功能(验证权限).
    
    实际项目中，装饰器的语法框架，直接复制过去，修改装饰器名称和新功能的内容就行
"""


# 验证权限
# def verif_permissions(func):
#     def wrapper(*args, **kwargs):
#         print("验证权限")
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @verif_permissions
# def insert():
#     print("插入成功")
#
#
# @verif_permissions
# def delete():
#     print("删除成功")
#
#
# insert()
# delete()






"""
    装饰器 - 细节语法
        1. 内部函数返回值是旧功能返回值
"""

#
# def print_func_name(func):
#     # *合:将多个位置实参合并为一个元组
#     # **合:将多个关键字实参合并为一个字典
#     def wrapper(*args, **kwargs):  # 2
#         print("-----", func.__name__, "-----")
#         # *拆：将一个序列拆分为多个元素
#         # **拆：将一个字典拆分为多个键值对
#         return func(*args, **kwargs)  # 3 5
#
#     return wrapper
#
#
# @print_func_name
# def func01(p1, p2):  # 4
#     print("func01执行,参数是:", p1, p2)
#     return 100
#
#
# # 调用内部函数wrapper
# re = func01(1, p2 = 2)  # 1 6
# print(re)  # 100
#







"""
    练习:使用装饰器，为旧功能增加新功能(验证权限)，
    旧功能有参数，装饰器是不用修改参数的，只需要改旧功能的参数
"""
#
# def verif_permissions(func):
#     def wrapper(*args, **kwargs):  # 合并insert(1,2, p3=3,p4=4)传入的信息
#         print("验证权限")
#         return func(*args, **kwargs)  # 拆后与旧功能对应
#
#     return wrapper
#
#
# @verif_permissions  # 一次接收
# def insert(p1, p2, p3, p4):
#     print(p1, p2, p3, p4)
#
#
# # 多次调用执行wrapper函数
# insert(1, 2, p3=3, p4=4)
# insert(1, 2, p3=3, p4=4)
# insert(1, 2, p3=3, p4=4)
#



"""

如果新增的功能，只是临时的，不是必须的，可以使用装饰器
如果新增的功能，是永久的，那直接写在老函数的函数体里面就行了

"""
