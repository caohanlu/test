
# def func01(p1,p2,p3):  #形参【就叫位置形参】
#     """
#     我是函数
#     :param p1:
#     :param p2:
#     :param p3:
#     :return:
#     """
#     print(p1)
#     print(p2)
#     print(p3)
#
#
# func01(1,2,3)  #位置实参,要跟形参的位置一一对应
#                # ctrl+p,提示参数数量
#                #ctrl+q,提示函数的备注
#
# func01(p3=1,p2=2,p1=3) #关键字实参，# 即写出形参的名字，然后赋值，
# func01(p3=1)           #可以给指定的形参传递参数，需要跟默认形参结合使用，否则报错
#





# def func01(p1=0, p2=0, p3=0):  # 默认形参，默认值必须从右到左，依次存在，如下
#         #(p1, p2=0, p3=0):
#         #(p1, p2, p3=0):
#     print(p1)
#     print(p2)
#     print(p3)
#
# func01(1,2)  #只给前两个参数传递参数
# func01(p3=1) #只给p3这个形参，传递参数
# func01(1,p3=1) #只给第一个参数、p3这个参数，传递参数




"""
序列实参，
也是位置实参的一种
使用*，拆解列表、字符串、元组里的元素，将元素跟形参一一对应，进行序列传参

"""
# def func01(p1, p2, p3):
#     print(p1)
#     print(p2)
#     print(p3)
#
# list01 = [1, 2, 3]
# str01 = "123"
# tuple01 = (1, 2, 3)
#
# func01(*list01)
# func01(*str01)
# func01(*tuple01)






"""
字典实参，
是关键字实参的一种
使用*×，拆解字典里的元素，字典的key必须跟形参一样,值就是给形参传递的数据

"""
# def func01(p1, p2, p3):
#     print(p1)
#     print(p2)
#     print(p3)
#
# dict01 = {"p1": 1, "p2": 2, "p3": 3}  #字典的key必须跟形参一样,值就是给形参传递的数据
#
# func01(**dict01)  #字典，需要两个**











"""
根据小时、分钟、秒，计算总秒数

"""
# def count_seconds(hour=0, min=0, sec=0):
#     return hour * 60 * 60 + min * 60 + sec
#
#
# print(count_seconds(1,1,1))  #提供小时、分钟、秒
# print(count_seconds(min=1, sec=1))#提供分钟、秒
# print(count_seconds(hour=1, sec=1))#提供小时、秒
# print(count_seconds(1, sec=1))     #提供小时、秒
# print(count_seconds(min=1))        #提供分钟







"""
命名关键字形参
    即*后面的形参,在传参的时候，要写成关键字实参
"""
# def func01(*args,p1,p2):
#     print(args)
#     print(p1)
#     print(p2)
#
# func01(1,2,3,p1=4,p2=5)    #p1,p2是命名关键字形参，实参要写成关键字实参
# print(1,2,3,end="",sep="__") #例如print(1,2,3,end=" ",sep="__"),end和sep就是命名关键字形参

#或者如下

# def fun01(p1, *, p2):
#     print(p1)
#     print(p2)
#
# fun01(1, p2=2)   #p2是命名关键字形参，实参要写成关键字实参







"""
星号元组形参【不定长形参】：即实参的数量不固定，将多个位置实参，合并成一个元组
                        给形参传递的数据是一个元组
                        只能有一个形参

"""
# def func01(*args):
#     print(args)
#
# func01()
# func01(1,2,3)
#


"""
多个数值累乘
"""
# def multiplicative(*args):
#     result = 1
#     for item in args:
#         result *= item
#     return result
#
#
# print(multiplicative(1,2,3,4))













"""
双星号字典形参【不定长形参】：即实参的数量不固定，将关键字实参合并为字典
              

"""
# def func01(**kwargs):
#     print(kwargs)
#
# func01()
# func01(a=1,b=2,c=3) #a,b,c是键，   1,2,3是值
#





"""
    调用下列函数
"""

# def func01(*args, **kwargs):  # 实参数量无限
#     print(args)
#     print(kwargs)
#
# func01()
# func01(1, 2, 3,4,a=5, b=6)







"""

参数自左至右的顺序
如果多个形参同时存在，需要按照如下的次序：
位置形参 --> 星号元组形参 --> 命名关键字形参 --> 双星号字典形参

"""
# p1:位置形参:必填
# p2:位置形参+默认形参:因为有默认值，所以可选
# args:星号元组形参：位置实参数量无限
# p3:命名关键字形参+默认形参:关键字实参(可选)，因为有默认值，所以可选
# kwargs:双星号字典形参：关键字实参数量无限

def func02(p1, p2="", *args, p3=0, **kwargs):
    print(p1)
    print(p2)
    print(args)
    print(p3)
    print(kwargs)

func02(1, 2, 3, 4, 5, p3=3, a=1, b=2)






