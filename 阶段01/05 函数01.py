"""
打印各元素，2 3 4 56
          a b c d
"""
# def func_print(parameter):
#     for item in parameter:
#         print(item, end=" ")
#
# list01 = [2, 3, 4, 56]
# list02 = ["a", "b", "c", "d"]
#
# func_print(list01)
# func_print(list02)





"""
打印如下，需要自己决定参数是什么，真是业务场景下，没人告你你
×××××
×××××
×××××
"""
# def func_print(row, column):
#     for r in range(row):
#         for c in range(column):
#             print("*", end="")
#         print()
#
#
# func_print(3, 5)




"""
美元到人民币的汇率转换器，要有函数返回值
"""
# def usd2rmb(usd):
#     rmb = float(usd) * 7.14
#     return rmb
#
# rmb = usd2rmb(3)
# print(rmb)





"""
收银台找零，
商品单价、数量、金额，显示需要找多少钱
"""
# def give_change(num, price, money):
#     """
#     函数写好后，需要在第一行，写三个双引号，回车，
#     则自动将参数按照如下格式显示出来，需要对函数和参数的功能进行备注
#     :param num:
#     :param price:
#     :param money:
#     :return:
#     """
#     return money - num * price
#
#
# num = input("输入数量：")
# price = input("输入单价：")
# money = input("输入金额：")
#
# givechange = give_change(int(num), float(price), float(money))
# print("找零:%.2f" % (givechange))





"""
一个函数只能有一个返回值
如果返回的数据很多，则可以使用容器

古代的秤，一斤等于十六两。
在终端中获取两，计算几斤零几两。
"""

# def liang2jin(amount):
#     jin = amount // 16
#     liang = amount % 16
#     return jin, liang    #元组，不写括号，也是元组
#
#
# amount = input("输入多少两：")
# print(liang2jin(int(amount)))






"""
    输入课程阶段数,显示课程名称
    1 显示 Python语言核心编程
    2 显示 Python高级软件技术
    3 显示 Web 全栈
    4 显示 网络爬虫
    5 显示 数据分析、人工智能
"""

# def get_course_name(num):
#     list_course_name = ["python语言核心编程",
#                         "Python高级软件技术",
#                         "Web 全栈",
#                         "网络爬虫",
#                         "数据分析、人工智能"
#                         ]
#     if 1 <= num <= 5:
#         return list_course_name[num - 1]
#     return "课程不存在"
#
#
# print(get_course_name(8))
#







"""
商品优惠
打折策略：如果vip客户，消费小于500,享受85折
                    否则享受8折
         否则，消费大于800,享受9折
               否则原价
根据账户类型和消费金额，计算折扣.
"""
# def commodity_discount(account_type, consumption_amount):
#     if account_type=="vip":
#         if consumption_amount < 500:
#             return 0.85
#         return 0.8      ##这里的else省略了，因为上面的return直接退出函数了，所以不需要再写else
#     else:
#         if consumption_amount > 800:
#             return 0.9
#         return 1
#
#
# print(commodity_discount("vip", 1000))
#






"""

如下，
函数只有通过键、索引、切片【字典、列表、集合】，修改传递来的变量时，外部变量才会被修改
否则修改的只是函数内部的变量，外部变量不会被修改【数值、字符串、元组等】

"""
# def func01(p1, p2, p3):
#     p1 = "孙悟空"  # 修改的只是函数内部的变量，外部变量a不会被修改
#     p2["八戒"] += 50  # 通过键修改，所以外部变量b会被修改
#     p3 = ["唐三藏"]  # 修改的只是函数内部的变量，外部变量c不会被修改
#
#
# a = "悟空"
# b = {"八戒": 100}
# c = ["唐僧", 200]
# func01(a, b, c)
# print(a)  # "悟空"
# print(b)  # {"八戒": 150}
# print(c)  # ["唐僧", 200]





"""
从小到大排序

"""
# def sort(list01):
#     for r in range(len(list01) - 1):
#         for c in range(r + 1, len(list01)):
#             if list01[r] > list01[c]:
#                 list01[r], list01[c] = list01[c], list01[r]
#
# list01 = [43, 15, 5, 67, 87, 9]
# sort(list01)  #被函数修改，函数不需要写return，直接修改了列表
# print(list01) #print被修改后的列表
#





"""
如果一个变量,多个函数都要使用，可以作为全局变量

按照如下格式写代码：
========================全局变量===========================
========================定义函数==========================
========================调用函数===========================

"""











