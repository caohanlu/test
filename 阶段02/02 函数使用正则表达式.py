"""
总结：

re 模块，使用正则表达式


使用下面6个函数，需要import re
   findall()   匹配
   split()     切割
   sub()       替换

下面三个函数，返回值是可迭代对象，match对象
    finditer()  根据正则表达式匹配目标字符串内容
    match()     被匹配到的内容，必须在目标字符串的开头位置
    search()    匹配目标字符串中，第一个符合正则表达式规则的内容

            match对象使用
                span()       获取匹配内容的起、止位置
                groupdict()  获取捕获组字典，组名为键，对应内容为值
                group(n = 0) 参数：默认为0表示获取整个match对象内容，如果是序列号或者组名，则表示获取对应子组内容



    https://tool.oschina.net/regex/#

"""








"""
 re.findall(pattern,string,flags = 0)
 功能: 根据正则表达式匹配目标字符串内容
 参数: pattern 正则表达式
      string  目标字符串
      flags   功能标志位,扩展正则表达式的匹配【默认是0，即不扩展】
 返回值: 匹配到的内容列表,是个列表
        如果正则表达式有子组，则只能获取到子组对应的内容

"""

import re

# s = "Alex:1998,Sunny:1997" # 目标字符串
# pattern = r"\w+:\d+" # 正则
# l = re.findall(pattern,s)
# print(l)
# ['Alex:1998', 'Sunny:1997']


# s = "Alex:1998,Sunny:1997"
# pattern = r"(\w+):\d+"
# l = re.findall(pattern,s)
# print(l)
# ['Alex', 'Sunny']   # 正则表达式有子组的时候，只获取子组对应的匹配内容，【别的被正则表达式匹配的内容，不获取】
# 这是findall函数的问题，而不是正则表达式的问题







"""
 re.split(pattern,string,max，flags = 0)
 功能: 使用正则表达式匹配到的内容【即分隔符】,来切割目标字符串
 参数: pattern   正则表达式
      string    目标字符串
      max       最多切割几处，不写，表示全部切割
      flags     功能标志位,扩展正则表达式的匹配
 返回值: 切割后的内容列表
"""
# s = "Alex:1998,Sunny:1997"
# l = re.split(r"\W+",s,2)   #2表示切割两处
# print(l)
# ['Alex', '1998', 'Sunny:1997']






"""

 re.sub(pattern,replace,string,count,flags = 0)
 功能: 使用一个字符串replace，替换正则表达式匹配到的内容
 参数: pattern  正则表达式
      replace  替换的字符串
      string 目标字符串
      count  最多替换几处,默认替换全部
      flags  功能标志位,扩展正则表达式的匹配
 返回值: 替换后的字符串

"""
# 使用\W+匹配目标字符串s，使用## 替换匹配到的内容
# s = "Alex:1998,Sunny:1997"
# s = re.sub(r"\W+",'##',s,2)
# print(s)
# Alex##1998##Sunny:1997







"""

下面三个函数，返回值是可迭代对象，match对象
    finditer()  根据正则表达式匹配目标字符串内容
    match()     被匹配到的内容，必须在目标字符串的开头位置
    search()    匹配目标字符串中，第一个符合正则表达式规则的内容

match对象使用
    span()       获取匹配内容的起、止位置
    groupdict()  获取捕获组字典，组名为键，对应内容为值
    group(n = 0) 参数：默认为0表示获取整个match对象内容，如果是序列号或者组名，则表示获取对应子组内容

"""




"""
 re.finditer(pattern,string,flags = 0)
 功能: 根据正则表达式匹配目标字符串内容
 参数: pattern  正则表达式
      string 目标字符串
      flags  功能标志位,扩展正则表达式的匹配
 返回值: 被匹配到的结果的迭代器
"""
# import re
#
# s = "Alex:1998,Sunny:1997"  # 目标字符串
# pattern = r"\w+:\d+"        # 正则
# l = re.finditer(pattern,s)  # 将匹配到的内容生成一个迭代对象
# for i in l:                 # 每次取出一个匹配内容对应的match对象
#     print(i.group())        # 获取match对象对应的内容
# Alex:1998
# Sunny:1997


# import re
#
# s = "Alex:1998,Sunny:1997"
# pattern = r"((\w+):(?P<year>\d+))"  #如果有分组，这里有三组括号，就是三个组
#                                     #  第一组((\w+):(\d+))   # 第二组(\w+)   # 第三组(?P<year>\d+)
# l = re.finditer(pattern,s)
# for i in l:
#     print(i.group(3))       # 获取match对象对应的内容中，指定分组的内容，这里获取第三组的内容
#    print(i.group('year'))  # 第三组通过名字获取也行
# 1998
# 1998
# 1997
# 1997




"""

re.match(pattern,string,flags=0)
功能：被匹配到的内容，必须在目标字符串的开头位置
参数：pattern 正则
	string  目标字符串
返回值：匹配内容match object

"""
# s = "Alex:1998,Sunny:1997"
# pattern = r"((\w+):(?P<year>\d+))"
# obj = re.match(pattern,s)
# print(obj.group())
# # Alex:1998





"""
re.search(pattern,string,flags=0)
功能：匹配目标字符串中，第一个符合正则表达式规则的内容
参数：pattern 正则
	string  目标字符串
返回值：匹配内容match object
"""
# s = "Alex:1998,Sunny:1997"
# pattern = r"((\w+):(?P<year>\d+))"
# obj = re.search(pattern,s)
# print(obj.group())
# Alex:1998   #由于Sunny:1997是子二个被匹配到的地方，所以没被获取到




"""
2.4.3 match对象使用

- span()       获取匹配内容的起、止位置
- groupdict()  获取捕获组字典，组名为键，对应内容为值
- group(n = 0) 参数：默认为0表示获取整个match对象内容，如果是序列号或者组名，则表示获取对应子组内容

"""
# s = "Alex:1998,Sunny:1997"
# pattern = r"((\w+):(?P<year>\d+))"
# obj = re.search(pattern,s)
# print(obj.group())  # 匹配到的内容 Alex:1998
# print(obj.span())   # 获取匹配到的内容在目标字符串中的位置(0, 9)
#                     # 通过位置对字符串切片，就是被匹配到的内容print(s[0:9])
# print(obj.groupdict())  # 捕获组组名和对应内容形成的字典 {'year': '1998'}







'''

2.4.4 flags参数扩展

作用函数：re模块调用的匹配函数。如：re.findall,re.search....

4个常用flag
  A == ASCII  元字符只能匹配ascii码【英文键盘能打出来的所有字符】
  I == IGNORECASE  匹配忽略字母大小写
  S == DOTALL  使 . 可以匹配换行
  M == MULTILINE  使 ^  $可以匹配每一行的开头结尾位置

  注意：同时使用多个flag，可以用竖线连接   flags = re.I | re.A

'''

import re

# 目标字符串，中英文加换行
# s = """Hello
# 北京
# """
#
# l = re.findall(r"\w+", s, flags=re.A)    # 让正则表达式只能匹配ascii码（英文符号）
# print(l)  # ['Hello']


# 目标字符串，中英文加换行
# s = """Hello
# 北京
# """
#
# 让 . 可以匹配换行
# l = re.findall(r".+", s, flags=re.S)
# print(l)    #['Hello\n北京\n']


# #目标字符串，中英文加换行
# s = """Hello
# 北京
# """
#
# # 忽略字母大小写
# l = re.findall(r"[a-z]+", s,flags=re.I)
# print(l)    #['Hello']


# #目标字符串，中英文加换行
# s = """Hello
# 北京
# """
#
# #让^ $ 可以匹配每一行的开头结尾位置
# #如果不加flags=re.M，则开头只是Hello，如果加了，虽然Hello后面换行了，才是北京，北京不是整个字符串的开头
# # 但是北京属于换行后的开头
# l = re.findall(r"^\w+", s,flags=re.M)
# print(l)        #['Hello', '北京']






"""
编写一个函数，参数传入一个设备端口名称
           返回值是这个端口描述中所对应的 mac address
         

         思路： 根据端口名确定段落
               再从段落中匹配目标

         提示： 段与段之间有空行
               每段第一个单词是端口名称
               端口名称可能很复杂
"""

# import re
#
#
# # 获取每个段落
# def get_info():
#     f = open("log.txt")
#
#     while True:
#         info = ""
#         for line in f:
#             if line == "\n":  # 这是一个空行，则退出for循环
#                 break
#             info += line  # 如果不是空行，则每行字符串拼接
#         if not info:  # 文件读完后，则for循环不再执行，如果info变量是空，结束while死循环
#             break
#         yield info
#
#     f.close()
#     return
#
#
# def get_address(port):
#     for data in get_info():
#         obj = re.match(r"\S+", data)  # 非空，并且在段落开头位置
#         if port == obj.group():
#             pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
#             result = re.search(pattern, data)
#             if result:
#                 return result.group()
#             else:
#                 return "Unknown"
#     return "port error"
#
#
# print(get_address("TenGigE0/0/2/3"))
