"""
字符串格式化

"我是%s,今年%.2d，体重%.2f"%(name,int(age),float(weight))
   字符串  整数   小数，保留两位小数

"""
# name = input("输入姓名：")
# age = input("输入年龄：")
# weight = input("输入体重：")
# print("我是%s,今年%.3d，体重%.3f" % (name, int(age), float(weight)))
# message = "我是%s,今年%.3d，体重%.3f" % (name, int(age), float(weight))





#追加、插入
# list_name_area=["中国","美国","日本"]
# list_name_add=["10","20","30"]

# list_name_area.append("英国")
# list_name_add.append("40")
# print(list_name_area)
# print(list_name_add)
#
# list_name_area.insert(1,"埃及")
# list_name_add.insert(1,"50")
# print(list_name_area)
# print(list_name_add)




"""
遍历、倒序、修改
"""
# list_name_area = ["中国", "美国", "日本", "埃及"]
#
# for item in list_name_area:
#     print(item)
#
# for i in range(len(list_name_area) - 1, -1, -1):
#     print(list_name_area[i])
#
# for i in range(len(list_name_area)):
#     list_name_area[i] = 0
# print(list_name_area)




"""
实现如下
*
**
***
**
*
"""
# list01=[1,2,3,2,1]
# for item in list01:
#     print("*"*item)
#
#

#累乘
# list01 = [1, 2, 3, 2, 1]
# result = 1
# for item in list01:
#     result *= item
# print(result)



#个位不是5或3的数字，存入另一个列表
# list01 = [25, 63, 27, 75, 70, 83, 27]
# result = []
# for item in list01:
#     if item % 10 != 5 and item % 10 != 3:
#         result.append(item)
# print(result)





"""
输入疫情地区名称，
如果输入为空，则停止输入
如果输入的地区已经存在，则显示已存在
最后倒序打印所有地区
"""
# list_regions = []
# while True:
#     region = input("输入地区名称")
#     if region == "":
#         break
#     if region in list_regions:
#         print("已存在")
#     else:
#         list_regions.append(region)
# for i in range(len(list_regions) - 1, -1, -1):
#     print(list_regions[i])



"""
输入三次确诊人数，使用内置函数，输出最大值、最小值、平均值
"""
# list_confirm_num = []
# for i in range(3):
#     list_confirm_num.append(int(input("输入第%d次确诊人数" % (i + 1))))
# print(list_confirm_num)
# print(max(list_confirm_num))
# print(min(list_confirm_num))
# print(sum(list_confirm_num) / len(list_confirm_num))
#
#
#




"""
输入疫情地区名称，
如果输入为空，则停止输入
如果输入的地区已经存在，则显示已存在
@@@@@@@@@@@@@@@最后打印列表成字符串，连接符是-
"""
# list_regions = []
# while True:
#     region = input("输入地区名称")
#     if region == "":
#         break
#     if region in list_regions:
#         print("已存在")
#     else:
#         list_regions.append(region)
# str_regions = ".".join(list_regions)
# print(str_regions)



"""
将英文语句，按照单词翻转，例如,
即字符串转换成列表，列表翻转后，再把列表转换成字符串
to have a
改成
a have to
"""



"""
列表推导式，如下两段代码 ，结果是一样的
"""

# list_result="to have a".split(" ")
# print(list_result)
# print(" ".join(list_result[::-1]))

# list01 = []
# for r in range(1, 8):
#     for c in range(1, 8):
#         for m in range(1, 8):
#             list01.append((r, c, m))   #列表里追加的元素，是元组
# print(list01)



# list01 = [(r, c, m) for r in range(1, 8) for c in range(1, 8) for m in range(1, 8)]
# print(list01)
#



"""
定义函数，将列表中奇数删除
    根据某种条件，删除容器中的多个元素，采用倒序删除，正序删除的话，容易漏删、索引越界
    删除的本质，是后一个元素，挤掉前一个元素的位置，
    比如先删0索引的元素，则原本索引1的元素，变成0，下一个循环从1开始，则原本索引1的元素就被漏掉了
"""
# list01 = [3, 7, 5, 6, 7, 8, 9, 13]
#
# def del_list(list_arge):
#     for i in range(len(list_arge) - 1, -1, -1):
#         if list_arge[i] % 2 == 1:
#             del list_arge[i]
#     print(list_arge)
#
# del_list(list01)
