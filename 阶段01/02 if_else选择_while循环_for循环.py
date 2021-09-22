# if int(input("请输入身高")) >= 180 and input("请输入你有钱吗") == "有" and input("请输入你帅吗") == "帅":
#     print("嫁给你")
# else:
#     print("不嫁给你")


# number = int(input("输入数字"))
# if number > 0:
#     print("正数")
# elif number == 0:
#     print("0")
# else:
#     print("负数")
#




# #比较大小
#
# number1 = int(input("输入数字1:"))
# number2 = int(input("输入数字2:"))
# number3 = int(input("输入数字3:"))
# number4 = int(input("输入数字4:"))
# max = number1
# if max < number2:
#     max = number2
# if max < number3:
#     max = number3
# if max < number4:
#     max = number4
# print("最大值是" + str(max))









#在终端显示0 1 2 3
# count = 0
# while count < 4:
#     print(count)
#     count += 1



#在终端中累加 1 3 5 7
# count = 1
# sum = 0
# while count < 8:
#     print(count)
#     sum += count
#     count += 2
# print(sum)




# # 一张纸厚0.01，折叠几次才能超过8844.43
# high = 0.01
# n = 0
# while (high < 8844.43):
#     high *= 2
#     n += 1
# print(n)




#猜测数字大小，最多猜三次
# import random
#
# num01 = random.randint(1, 5)
# count01 = 0
#
# while count01<3:
#     count01 += 1
#     num02 = int(input("输入数字："))
#     if num02 > num01:
#         print("大了")
#     elif num02 < num01:
#         print("小了")
#     else:
#         print("答对了，一共猜了"+str(count01)+"次")
#         break
# else:
#     print("游戏失败")












#for 语句，用来遍历可迭代对象
#输入数字，计算每位相加之和
# num = input("输入数字")
# sum = 0
# for item in num:
#     sum += int(item)
# print(sum)


#range,整数生成器，开始，结束，间隔
# sum = 0
# for item in range(0, 7, 1):
#     if item % 2 ==0:
#         print(item)
#         sum += item
# print(sum)

#输入5个数字，求和
# sum = 0
# for item in range(5):
#         sum += int(input("输入数字"))
# print(sum)




"""
for循环的嵌套，解决平面问题，例如列表的嵌套
外层循环，控制行数r，内层循环，控制列c
"""

#输出五行七列*
# for r in range(5):
#         for c in range(7):
#                 print("*", end=" ")  # 以空格结束，默认是换行，这样就不换行
#         print()  # 换行



#二维列表  列表名[行索引][列索引]
list01=[[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15]
        ]
# 打印5 9 12
# print(list01[0][-1])
# print(list01[1][-2])
# print(list01[2][1])

# 打印6 7 8 9 10,每行一个数字
# for item in list01[1]:
#         print(item)

# 打印15 14 13 12 11,每行一个数字
# for i in range(len(list01[2]) - 1, -1, -1):
#         print(list01[2][i])

# 打印1 6 11,每行一个数字
# for r in range(3):
#         print(list01[r][0])

# 打印14 9 4,每行一个数字
# for r in range(2,-1,-1):
#         print(list01[r][-2])


# 以表格形状打印每个元素
# for r in range(len(list01)):
#         for c in range(len(list01[r])):
#                 print(list01[r][c],end=" ")
#         print()
#或
# for r in list01:
#         for c in r:
#                 print(c,end=" ")
#         print()

