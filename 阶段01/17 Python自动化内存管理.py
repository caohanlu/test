"""

        Python自动化内存管理
            引用计数:每个对象记录被变量绑定(引用)的数量,
                    当为0时被销毁。【被标记为不再使用，分代回收之后，才会被清除】
                缺点:循环引用 - 两个垃圾数据互相引用
                时机:时刻

            标记清除:"全盘"扫描内存,检查、标记不再使用的数据.
                缺点:效率太低
                时机:内存告急

            分代回收:将内存分为小中大【012】三代
                    每次创建新数据都在0代分配空间
                    当内存告急、标记清除后,将前一代有用的数据升级到下一代.
                    前一代所有数据清空


        上面三种是python自动实现的，下面是我们能做的：
        内存优化:
                尽少产生垃圾/自定义对象池【类】/控制内存管理系统的参数【一般不改】
                对象池:每当创建对象时,在池中判断是否存在相同对象,
                      如果有直接返回地址
                      如果没有再分配空间创建对象
                      例如,字符串池/整数池/小数池.....
                      价值:提高内存利用率


"""
# # 循环引用
# list01 = []
# list02 = []
# list01.append(list02)
# list02.append(list01)
# del list01, list02   #此时变量list01  list02被删了，
#                      # 但是list01  list02指向的列表互相引用，引用计数都是1，这两个列表没有被删除，占用内存空间，造成内存泄露
#
#
#
#
#
# # 产生垃圾的常用代码:
# a = "数据1"
# a = "数据2"  # 当变量a又指向"数据2"时,"数据1"成为垃圾.
#
# b = "数据3"
# del b  # 因为变量b被销毁,所以"数据3"成为垃圾
#
#
#
#
#
# # 根据某些逻辑,循环拼接字符串.(频繁修改字符串、元组等)
# str_result = ""
# for number in range(10):
#     str_result = str_result + str(number)    # 两个不可变对象,相加后会产生新对象
# print(str_result)
#
# # 解决:使用可变对象代替不可变对象
# list_result = []
# for number in range(10):
#     list_result.append(str(number))
# str_result = "".join(list_result) #再把列表变成字符串
# print(str_result)
#
#
#
# # 对象池:
# # 每当创建对象时, 在池中判断是否存在相同对象,
# # 如果有直接返回地址， 如果没有再分配空间创建对象
# # 例如, 字符串池 / 整数池 / 小数池.....
# # 价值: 提高内存利用率
# data01 = "悟空"
# data02 = "悟空"   #data01  02  指向的是同一个内存地址，就是字符串"悟空"的内存地址
# print(id(data01))
# print(id(data02))
#
#






# def func01():
#     for r in range(5):  # 执行一次
#         for c in range(4):  # 执行多次
#             # continue # 跳过当次循环
#             # break 跳出内层循环
#             return  # 结束函数(跳出所有循环)



