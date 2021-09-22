"""
字典
"""
#
#dict_beijing = {"地区": "北京", "新增": 4, "现有": 5, "累计": 6}
# dict_shanghai = {"地区": "上海", "新增": 7, "现有": 8, "累计": 9}
# dict_guangzhou = {"地区": "广州", "新增": 10, "现有": 11, "累计": 12}
#
# dict_beijing["死亡"] = 100
# dict_shanghai["死亡"] = 100
# dict_guangzhou["死亡"] = 100
#
# print(dict_beijing)
# print(dict_shanghai)
# print(dict_guangzhou)
#
# print("%s地区，新增%d，现有%d，累计%d，死亡%d"
#       % (dict_beijing["地区"],
#          dict_beijing["新增"],
#          dict_beijing["现有"],
#          dict_beijing["累计"],
#          dict_beijing["死亡"]
#          )
#


"""
两个列表，合并成一个字典，一个列表元素当键，一个列表元素当值
然后将字典的键、值颠倒，就可以根据值，找到对应的键

"""
# list_room = [101, 102, 103]
# list_name = ["张无忌", "赵敏", "周芷若"]
# dict01 = {}
# for i in range(0, 3):
#     dict01[list_room[i]] = list_name[i]
# print(dict01)
#
# dict_result = {}
# for k, v in dict01.items():    #遍历字典
#     dict_result[v] = k         #颠倒值、键
# print(dict_result)



"""
集合set
"""
# set_manager01 = {"张三", "李四", "王五"}
# set_tech01 = {"王五", "曹操", "刘备"}
# print(set_manager01)
# print(set_tech01)
# # 是经理也是技术
# print(set_manager01 & set_tech01)
# # 是经理，不是技术
# print(set_manager01 - set_tech01)
# # 身兼一职的
# print(set_manager01 ^ set_tech01)
# # 总人数
# print(len(set_manager01 | set_tech01))





"""
综合练习
比较160  170   180   190的最大值
"""
# list01 = [160, 170, 180, 190]
# max_value = list01[0]
# for i in range(1, len(list01)):
#     if max_value < list01[i]:
#         max_value = list01[i]
# print(max_value)






"""
自定义排序，
例如从大到小，则第一个元素，依次跟后面所有元素比较，取最大值，交换位置
              第二个元素，依次跟后面所有元素比较，取最第二大值，
              一直到倒数第二个元素，最后一个元素肯定是最小值
"""
# list01 = [12, 1, 0, 45, 123, 98, 66, 0, 9, 1234]
# for r in range(len(list01) - 1):  ###前面所有值，只取到倒数第二个值
#     for c in range(r + 1, len(list01)):  ##跟后面所有的值比较，要取到最后一个值
#         if list01[r] < list01[c]:  ###前一个值小于后一个值的话，两个值交换位置
#             list01[r], list01[c] = list01[c], list01[r]
# print(list01)
#
#






"""
综合练习
商品处理
"""
# 商品字典
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}

# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]




# 1.打印所有商品信息,
# 格式：商品编号xx,商品名称xx,商品单价xx.
#for key,value in dict_commodity_infos.items():
    #print("商品编号:"+str(key)+",商品名称:"+value["name"]+",商品单价:"+str(value["price"]))
    #print("商品编号%d,商品名称%s,商品单价%d"%(key,value["name"],value["price"]))

# 2. 打印所有订单中的信息,
# 格式：商品编号xx,购买数量xx.
# for item in list_orders:
#     print("商品编号%d，购买数量%d"%(item["cid"],item["count"]))

# 3. 打印商品单价小于2万的商品信息
#  格式：商品编号xx,商品名称xx,商品单价xx.
# for key, value in dict_commodity_infos.items():
#     if value["price"] < 20000:
#         print("商品编号%d,商品名称%s,商品单价%d" % (key, value["name"], value["price"]))


# 4. 打印所有订单中的商品信息,
#    格式：商品名称xx,商品单价:xx,数量xx.
# for item in list_orders:
#     print("商品名称:%s，商品单价:%d，商品数量:%d" % (
#     dict_commodity_infos[item["cid"]]["name"], dict_commodity_infos[item["cid"]]["price"], item["count"]))



# 5. 查找数量最多的订单(使用自定义算法,不使用内置函数)
# max_count = list_orders[0]
# for i in range(1, len(list_orders)):
#     if max_count["count"] < list_orders[i]["count"]:
#         max_count = list_orders[i]
# print(max_count)




# 6. 根据购买数量对订单列表降序(大->小)排列
# for r in range(len(list_orders) - 1):  ###前面所有值，只取到倒数第二个值
#     for c in range(r + 1, len(list_orders)):  ##跟后面所有的值比较，要取到最后一个值
#         if list_orders[r]["count"] < list_orders[c]["count"]:  ###前一个值小于后一个值的话，两个值交换位置
#             list_orders[r], list_orders[c] = list_orders[c], list_orders[r]
# print(list_orders)





"""
综合练习

"""
dict_hobbies = {
    "qtx": ["看书", "编码", "旅游"],
    "lzmly": ["刷抖音", "看电影"],
    "于谦": ["抽烟", "喝酒", "烫头"]
}
# 打印"于谦"的第二个爱好
#print(dict_hobbies["于谦"][1])

# 打印qtx所有爱好(一行一个)
# for item in dict_hobbies["qtx"]:
#     print(item)

# 打印lzmly的爱好数量
# count=0
# for item in dict_hobbies["lzmly"]:
#     count+=1
# print(count)
#或者如下
#print(len(dict_hobbies["lzmly"]))



# 打印所有人的所有爱好(一行一个)
# for value in dict_hobbies.values():
#     for item in value:
#         print(item)






"""
综合练习

"""
dict_travel_info = {
    "北京": {
        "景区": ["长城", "故宫"],
        "美食": ["烤鸭", "豆汁胶圈", "炸酱面"]
    },
    "四川": {
        "景区": ["九寨沟", "峨眉山"],
        "美食": ["火锅", "兔头"]
    }
}

# 1)打印所有城市（一行一个）
# for key in dict_travel_info:
#     print(key)

# 2)打印北京所有美食（一行一个）
# for item in dict_travel_info["北京"]["美食"]:
#     print(item)

# 3)打印四川所有景区（一行一个）
# for item in dict_travel_info["四川"]["景区"]:
#     print(item)


# 4)打印所有城市的所有景区（一行一个）
# for key in dict_travel_info:
#     for value in dict_travel_info[key]["景区"]:
#             print(value)

# 5)为北京添加景区："天坛"
# dict_travel_info["北京"]["景区"].append("天坛")
# print(dict_travel_info["北京"]["景区"])


# 6)删除四川美食：兔头
# dict_travel_info["四川"]["美食"].remove("兔头")
# print(dict_travel_info["四川"]["美食"])












"""
综合练习

"""
# 员工列表(员工编号 部门编号 姓名 工资)
dict_employees = {
    1001: {"did": 9002, "name": "师父", "money": 60000},
    1002: {"did": 9001, "name": "孙悟空", "money": 50000},
    1003: {"did": 9002, "name": "猪八戒", "money": 20000},
    1004: {"did": 9001, "name": "沙僧", "money": 30000},
    1005: {"did": 9001, "name": "小白龙", "money": 15000},
}

# 部门列表
list_departments = [
    {"did": 9001, "title": "教学部"},
    {"did": 9002, "title": "销售部"},
    {"did": 9003, "title": "品保部"},
]


# 1. 打印所有员工信息,
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
# for key, value in dict_employees.items():
#     print("%s的员工编号是%d，部门编号是%d，月薪%d元." % (value["name"], key, value["did"], value["money"]))



# 2. 打印所有月薪大于2w的员工信息,
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
# for key, value in dict_employees.items():
#     if value["money"] > 20000:
#         print("%s的员工编号是%d，部门编号是%d，月薪%d元." % (value["name"], key, value["did"], value["money"]))

# 3. 在部门列表中查找编号最小的部门
# min = list_departments[0]
# for i in range(1, len(list_departments)):
#     if min["did"] > list_departments[i]["did"]:
#         min = list_departments[i]
# print(min)

# 4.  根据部门编号对部门列表降序排列
# for r in range(len(list_departments) - 1):
#     for c in range(r + 1, len(list_departments)):
#         if list_departments[r]["did"] < list_departments[c]["did"]:
#             list_departments[r], list_departments[c] = list_departments[c], list_departments[r]
# print(list_departments)



