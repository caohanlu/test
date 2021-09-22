'''
 多核CPU：现在的计算机一般都是多核CPU，比如四核，八核，我们可以理解为由多个单核CPU的集合。
        操作系统可以将多个任务分配给某一个cpu核心，也可以将多个任务分配给多个cpu核心，
        操作系统会自动根据任务的复杂程度选择最优的分配方案。

        * 并发 ：
            多个任务如果被分配给了一个cpu内核，那么这多个任务之间就是并发关系，并发关系的多个任务之间并不是真正的‘"同时",而是cpu轮训。
        * 并行 ：
            多个任务如果被分配给了不同的cpu内核，那么这多个任务之间执行时就是并行关系，并行关系的多个任务时真正的“同时”执行。


* 并发、并行，都是多任务



* 什么是多任务编程
  即一个程序中编写多个任务，在程序运行时，让这多个任务一起运行，而不是一个一个的顺次执行。
  比如微信视频聊天，这时候在微信运行过程中既用到了视频任务，也用到了音频任务，甚至同时还能发消息。
  这就是典型的多任务。而实际的开发过程中这样的情况比比皆是。




* 多任务意义
  * 提高了任务之间的配合，可以根据运行情况进行任务创建。
    比如： 你也不知道用户在微信使用中是否会进行视频聊天，总不能提前启动起来吧，这是需要根据用户的行为启动新任务。

  * 充分利用计算机资源，提高了任务的执行效率。
    * 阻塞状态不占用cpu，例如sleep，tcp accept，tcp udp的recv等
    * 在任务中无阻塞时只有并行状态才能提高效率
        因为cpu轮训，并不能减小程序的执行时间
    * 在任务中有阻塞时并行并发都能提高效率
        因为程序等待的时间，cpu可以去处理别的任务






* 实现多任务编程的方法 ：
    多进程编程;
    多线程编程;







2.2 进程（Process）
定义： 程序在计算机中的一次执行过程。
  - 程序是一个可执行的文件，是静态的,只占有磁盘。
  - 进程是一个动态的过程描述，占有计算机运行资源cpu内存等，有一定的生命周期。
        程序运行起来就是进程。

进程状态
  三态
     就绪态 ： 进程具备执行条件，等待系统调度分配cpu资源
     运行态 ： 进程占有cpu正在运行
     等待态 ： 进程阻塞等待【例如IO请求】，此时会让出cpu



  五态 (在三态基础上增加新建和终止)
     新建 ： 创建一个进程，获取资源的过程
     终止 ： 进程结束，释放资源的过程



进程命令
  * linux查看进程信息：
   ps -aux

    root@caohanlu:~/PycharmProjects/pythonProject/网络编程_单进程_循环# ps -aux
    USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
    root         1  0.0  0.0 225760  8380 ?        Ss   Apr15   4:59 /lib/systemd/systemd --system --deserialize 39
    root         2  0.0  0.0      0     0 ?        S    Apr15   0:03 [kthreadd]
    root         4  0.0  0.0      0     0 ?        I<   Apr15   0:00 [kworker/0:0H]
    root         5  0.0  0.0      0     0 ?        I    Apr15   0:01 [kworker/u32:0]

    * USER ： 进程的创建者
    * PID  :  操作系统分配给进程的编号,大于0的整数，系统中每个进程的PID都不重复。PID也是重要的区分进程的标志。
    * %CPU,%MEM : 占有的CPU和内存
    * STAT ： 进程状态信息，S I 表示阻塞状态  ，R 表示就绪状态或者运行状态
    * START : 进程启动时间
    * COMMAND : 通过什么程序启动的进程



  * 进程树形结构
    pstree
        * 父子进程：在Linux操作系统中，进程形成树形关系，任务上一级进程是下一级的父进程，下一级进程是上一级的子进程。






2.2.2 多进程编程
* 使用模块 ： multiprocessing

* 创建流程
  【1】 将需要新进程执行的事件封装为函数
  【2】 通过模块的Process类创建进程对象，关联函数
  【3】 可选，可以通过进程对象设置进程信息及属性
  【4】 通过进程对象调用start启动进程
  【5】 通过进程对象调用join回收进程资源





* 主要类和函数使用
Process()
功能 ： 创建进程对象
参数 ： target 绑定要执行的目标函数
	   args 元组，用于给target函数位置传参
	   kwargs 字典，给target函数键值传参


p.start()
功能 ： 启动进程
    > 注意 : 启动进程，此时target绑定函数开始执行，该函数作为新进程执行内容，此时进程真正被创建


p.join([timeout])
功能：父进程，阻塞等待、回收进程
参数：超时时间，不写就是一直等，假如写3，则最多等3s，3s后就不等了，就不回收，即交给操作系统回收


'''






"""
进程创建过程
1. 将需要新进程执行的事件封装为函数
2. 通过模块的Process类创建进程对象，关联函数
3. 通过进程对象调用start启动进程
4. 通过进程对象调用join回收进程资源

* 进程执行现象理解 （难点）
  * 新的进程是原有进程的子进程，子进程复制父进程全部内存空间代码段，复制到另一个内存空间，一个进程可以创建多个子进程。
  * 子进程只执行指定的函数，其余代码内容均是父进程执行内容，但是子进程也拥有父进程的其他资源。
  * 各个进程在执行上互不影响，也没有先后顺序关系。
  * 进程创建后，各个进程内存空间独立，相互没有影响。
  * multiprocessing 创建的子进程中无法使用标准输入（input）。
"""
#
# import multiprocessing
# from time import sleep
#
# a = 10
#
# # 将需要新进程执行的事件，封装为函数
# def fun():
#     print("子进程，开始执行进程函数。。。")
#     global a
#     print("子进程，a =",a)  #10,由于子进程复制了父进程全部代码，所以子进程可以修改全局变量a，
#                            # 但是由于父进程、子进程，是完全独立的两个内存空间，
#                            #所以子进程修改的a， 其实是子进程的a，所以父进程的a在父进程里是不会被子进程改变的
#     a = 10000
#     sleep(2)
#     print("子进程，a =", a)    #10000
#     print("子进程，进程函数执行完了")
#
#
# # 通过模块的Process类，创建进程对象，关联函数
# # 这个py文件执行时，本身就是一个进程【父进程】，由于py文件里又创建了一个进程【子进程】，则一共两个进程
# # target=fun不能加括号，因为传递的是函数名，而不是调用函数
# p = multiprocessing.Process(target=fun)
#
#
# # 启动进程，执行fun函数内容
# p.start()
#
#
# #  如果希望子进程里的函数执行任务，同时这个python文件本身父进程也执行任务，即多任务同时执行
# # 【至于是并发还是并行，这个不确定，因为由操作系统决定，并且父子进程抢占cpu时间片，不一定是父进程先执行任务，还是子进程先执行】
# #  需要在start之后【启动进程了，函数内容才能执行】，
# #  join之前【如果写在join之后，则需要一直等待子进程执行完了之后，这个python文件本身父进程才能执行想要做的事】，
# #  写上想要做的事的代码就行，如下
# print("父进程，原来的父进程做点事")
# sleep(2)
# print("父进程，事情干完了")
#
#
#
# # 父进程，通过进程对象调用join，等待执行完后回收进程资源，
# p.join()
#
#
# print("父进程，a:",a)   #父进程的a还是10，不会被子进程改变
#









"""
包含参数的进程函数演示
"""
# from multiprocessing import Process
# from time import sleep
#
# # 带有参数的进程函数
# def worker(sec,name):
#     for i in range(3):
#         sleep(sec)
#         print("I'm %s"%name)
#         print("I'm working...")
#
# # 位置传参
# p = Process(target=worker,args=(1,"Levi"))
#
# # 或者关键字传参
# # 这里混搭了，靠前的参数使用元组，并且要加上逗号，哪怕只有一个值，也要加逗号，因为是元组
# # p = Process(target=worker,args=(1,),kwargs={"name":"Baron"})
#
#
# p.start()
#
# #由于子进程需要3s执行完，但是join只等2s，所以2s后，父进程执行完下面的print，就结束了
# #则等到子进程执行完后，由操作系统回收子进程
# #但是如果父进程不结束，则子进程结束后，会等待父进程回收，而不是系统回收子进程
# p.join(2)
# print("=========================================")
#






"""
练习1： 大文件拆分
将一个文件拆分为两个部分，每个部分分别是文件大小的一半
即源文件的上、下两部分，分别拆到两个新文件里
要求使用两个进程同时进行

提示： 按照文件的字节数计算文件大小
      os.path.getsize()

思路： 获取图片的大小  上 下两个部分的拆分分别封装为函数
"""
# from multiprocessing import Process
# import os
#
# size = os.path.getsize("sg.jpeg")  # 获取文件大小
#
# # 复制上半部分
# def top():
#     fr = open("sg.jpeg", 'rb')
#     fw = open("top.jpg", 'wb')
#     n = size // 2  # 要拷贝n个字节
#     while n >= 1024:
#         fw.write(fr.read(1024))
#         n -= 1024
#     else:
#         fw.write(fr.read(n))
#     fr.close()
#     fw.close()
#
#
# # 复制下半部分
# def bot():
#     fr = open("sg.jpeg",'rb')
#     fw = open("bot.jpg", 'wb')
#     fr.seek(size // 2, 0)  # 文件偏移量到中间
#     while True:
#         data = fr.read(1024)
#         if not data:
#             break
#         fw.write(data)
#     fr.close()
#     fw.close()
#
# p = Process(target=top) #　子进程执行一个
# p.start()
# bot() # 父进程同时执行一个
# p.join()
#







'''

* 进程对象属性
  * p.name          进程名称,可以自己命名，也可以不命名，系统会自己创建
  * p.pid           对应子进程的PID号
  * p.is_alive()    查看子进程是否在生命周期，
                    【是的话就是true，如果子进程已经执行完了，就是false】
                    
  * p.daemon     设置父子进程的退出关系【正常情况下，父进程结束，不会影响到子进程】
                * 如果设置为True【默认是false，也就是不设置】，
                  则该子进程会随父进程的退出而结束，【例如微信都崩了，还调用摄像头也没啥意义了】
                * 要求必须在start()前设置
                * 如果daemon设置成True 通常就不会使用 join()  
                 【该子进程会随父进程的退出而结束，根本不用等到子进程执行完毕，子进程就随着父进程的退出而退出】
    
'''
"""
进程属性设置演示
"""
# from multiprocessing import Process
# import time
#
# def fun():
#     for i in range(3):
#         print(time.ctime())
#         time.sleep(2)
#
# # 创建进程
# p = Process(target = fun,name = "print_time")
#
# # 该子进程会随父进程退出而退出
# # 在start前设置
# p.daemon = True
#
# p.start() # 进程启动
#
# print("p.name:",p.name)
# print("p.pid:",p.pid)
# print("p.is_alive:",p.is_alive())










'''
2.2.3 进程处理细节

* 进程相关函数

os.getpid()
功能： 获取一个进程的PID值
返回值： 返回当前进程的PID

os.getppid()
功能： 获取父进程的PID号
返回值： 返回父进程PID

sys.exit(info)
功能：退出进程
参数：字符串 表示退出时打印内容

'''

"""
进程相关小函数

循环创建多个子进程，如下
    但是如果每个子进程需要传参，就不能这样了
    

"""
#
# from multiprocessing import Process
# from time import sleep
# import  os,sys
#
# def th1():
#     sleep(1)
#     print("吃饭")
#     print(os.getppid(),'---',os.getpid())
#
# def th2():
#     sys.exit("不睡觉了")
#     sleep(1)
#     print("睡觉")
#     print(os.getppid(),'---',os.getpid())
#
# def th3():
#     sleep(1)
#     print("打豆豆")
#     print(os.getppid(),'---',os.getpid())
#
# things = [th1,th2,th3]
#
# jobs = [] # 用于存储启动的进程对象
#
# # 循环创建进程
# for th in things:
#     p = Process(target = th)
#     jobs.append(p)
#     p.start()    #for循环执行很快，可以认为三个进程同时开始执行，抢占cpu时间，哪个子进程先执行结束，完全取决于每个子进程的执行时间
#
# # 统一回收进程对象
# for i in jobs:
#     i.join()
#












'''
* 孤儿进程 ： 父进程先于子进程退出，此时子进程成为孤儿进程。
* 特点：      孤儿进程会被系统进程收养，此时系统进程就会成为孤儿进程新的父进程，
             孤儿进程退出后，该进程会由操作系统回收。

* 僵尸进程 ： 子进程先于父进程退出，父进程又没有回收子进程，并且父进程也没结束，
             则操作系统也没办法回收子进程，此时子进程就会称为僵尸进程。
* 特点：      僵尸进程虽然结束，但是会存留部分进程信息资源在内存中，大量的僵尸进程会浪费系统的内存资源。

* 如何避免僵尸进程产生
      1. 父进程使用join()回收
        一般，多个任务，就创建多个子进程去执行，父进程只用来回收子进程
        这个用的比下面那个方法多
      
      2. 在父进程中使用signal方法处理
      僵尸的本质是，子进程结束后，向父进程发出退出信号，
      signal方法就是，父进程忽略子进程退出信号，由系统处理子进程的退出信号
        
         from signal import *
         signal(SIGCHLD,SIG_IGN)

'''

"""
演示僵尸进程
"""
# from multiprocessing import Process
# import os,time
# from signal import *
#
# def fun():
#     for i in range(3):
#         print(os.getpid())
#         time.sleep(1)
#
# # 父进程忽略子进程退出信号，由系统处理，回收子进程
# signal(SIGCHLD,SIG_IGN)
#
# # 创建进程
# p = Process(target = fun,name = "print_time")
# p.start()
#
# while True:  #父进程死循环，无法结束所以操作系统无法回收子进程；同时循环之前又没join回收子进程，所以产生僵尸进程
#     pass









'''
上面，是将子进程执行的内容，封装为函数。
下面，也可以使用类，来封装进程执行的内容。




#### 2.2.5 创建进程类

* 创建步骤
  【1】 继承Process类
  【2】 重写`__init__`方法添加自己的属性，使用super()加载父类属性
  【3】 重写run()方法【进程调用start时，就运行run函数】

* 使用方法
  【1】 实例化对象
  【2】 调用start自动执行run方法
  【3】 调用join回收进程

'''
"""
自定义进程类
"""
# from multiprocessing import Process
#
# # 自定义类
# class MyProcess(Process):
#     def __init__(self,val):
#         self.val = val
#         super().__init__()  # 如果需要增加自己的属性，则需要重写init，并且加载父类属性
#
#     def fun1(self):                           #这两个函数可以不写
#         print("步骤1：假设很复杂",self.val)
#
#     def fun2(self):
#         print("步骤2：假设也很复杂",self.val)
#
#
#     def run(self):        # 重写run，将其作为一个新进程的执行内容，调用start时，就运行run函数
#         self.fun1()
#         self.fun2()
#
# process = MyProcess(2)
# process.start() # 启动进程 执行run()
# process.join()



'''

练习1 ： 编写一个程序
* 使用单进程，即不创建子进程 ,求100000以内质数之和  记录所用时间
* 使用4个进程，将100000拆分为4份，分别求每部分中质数之和 记录时间
* 使用10个进程，将100000拆分为10份，分别求每部分中质数之和 记录时间

'''


'''
* 使用单进程，即不创建子进程 ,求100000以内质数之和  记录所用时间
'''
#
# import time
#
#
# # 判断一个数是不是质数
# def isPrime(n):
#     if n <= 1:
#         return False
#     for i in range(2,n):
#         if n % i == 0:     #有个能整除的，就不是质数
#             return False
#     return True
#
#
# # 装饰器，求函数运行时间
# def timeis(f):
#     def wrapper(*args,**kwargs):
#         start_time = time.time()    #求和之前时间戳
#         res = f(*args,**kwargs)     #开始求和
#         end_time = time.time()      #求和之后时间戳
#         print("执行时间:",end_time - start_time)  #求和总时间
#         return res
#     return  wrapper
#
#
# #求质数之和
# @timeis
# def no_process():
#     prime = []
#     for i in range(1,100001):
#         if isPrime(i):
#             prime.append(i) # 将质数加入列表
#     print(sum(prime))
#
# no_process() # 执行时间: 25.926925897598267
#








'''

练习1 ： 编写一个程序
* 使用单进程，即不创建子进程 ,求100000以内质数之和  记录所用时间
* 使用4个进程，将100000拆分为4份，分别求每部分中质数之和 记录时间
* 使用10个进程，将100000拆分为10份，分别求每部分中质数之和 记录时间
'''
#
# import time
# from multiprocessing import Process
#
# # 判断一个数是不是质数
# def isPrime(n):
#     if n <= 1:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
#
# # 装饰器，求函数运行时间
# def timeis(f):
#     def wrapper(*args,**kwargs):
#         start_time = time.time()    #求和之前时间戳
#         res = f(*args,**kwargs)     #开始求和
#         end_time = time.time()      #求和之后时间戳
#         print("执行时间:",end_time - start_time)  #求和总时间
#         return res
#     return  wrapper
#
# #自定义类，创建进程
# class Prime(Process):
#     def __init__(self,begin,end):
#         """
#         :param begin: 开始数值
#         :param end: 结尾数值
#         """
#         self.begin = begin
#         self.end = end
#         super().__init__()
#
#     def run(self):
#         prime = []
#         for i in range(self.begin,self.end):
#             if isPrime(i):
#                 prime.append(i)
#         print(sum(prime))
#
#
# @timeis
# def process_4():
#     jobs = []
#     for i in range(1,100001,25000):
#         p = Prime(i,i+25000)
#         jobs.append(p)
#         p.start()
#     for i in jobs:
#         i.join()
#
# process_4() # 执行时间: 15.002186059951782
#
# # @timeis
# # def process_10():
# #     jobs = []
# #     for i in range(1,100001,10000):
# #         p = Prime(i,i+10000)
# #         jobs.append(p)
# #         p.start()
# #     for i in jobs:
# #         i.join()
# #
# # process_10() # 执行时间: 13.301548480987549




'''

如上，随着进程数量增加，处理时间有所减少，但是并没有成倍减少，
因为这些程序没有阻塞，并且cpu的数量是一定的，进程数量再多，但是cpu还是那么多，
所以进程数量，跟cpu核数差不多就行

'''












'''

#### 2.2.4 进程池
* 必要性
  【1】 进程的创建和销毁过程，消耗的资源较多
  【2】 当任务量众多，每个任务在很短时间内完成时，需要频繁的创建和销毁进程，此时对计算机压力较大
  【3】 进程池技术很好的解决了以上问题。

* 原理
  创建一定数量的进程【一般跟cpu核数差不多】来处理事件，事件处理完后，进程不退出，
  而是继续处理其他事件，直到所有事件全都处理完毕统一销毁。
  增加进程的重复利用，降低资源消耗。



* 进程池实现

1. 创建进程池对象，放入适当的进程

from multiprocessing import Pool

Pool(processes)
功能： 创建进程池对象
参数： 指定进程数量，默认根据系统自动判定【一般跟cpu核数差不多】


2. 将事件加入进程池队列、执行
pool.apply_async(func,args,kwds)
功能: 使用进程池执行函数func事件
参数： func 事件函数
      args 元组  给func按位置传参
      kwds 字典  给func按照键值传参


3. 关闭进程池
pool.close()
功能： 关闭进程池，【即不能往进程池增加新的任务函数func来执行，但是已经在进程池里的任务函数会继续执行】


4. 回收进程池中进程
pool.join()
功能： 回收进程池中进程


'''

"""

进程池使用示例
* 如果父进程退出，进程池自动销毁
* 事件函数的声明要在创建进程池之前

"""
#
# from multiprocessing import Pool
# from time import sleep,ctime
#
# # 进程池要执行的任务、或事件、或函数
# # 事件函数的声明要在创建进程池之前
# def worker(msg,sec):
#     print(ctime(),'---',msg)
#     sleep(sec)
#
# # 创建进程池，例如四个子进程
# pool = Pool(4)
#
# # 向进程池中加入事件、并执行
# # 循环调用同一个函数，通过给函数传递不同的参数，模拟多个任务
# # for循环很快，可以看成多个任务是同时添加到进程池，抢占cpu
# for i in range(10):
#     msg = "Tedu-%d"%i
#     pool.apply_async(func=worker,args=(msg,1)) # 事件开始执行
#
# pool.close()  # 关闭进程池，不能添加新的事件
# pool.join()   # 等事件都执行完，回收进程池
#               #join必须写，否则父进程结束后，进程池里的子进程即使没执行玩，也会自动销毁






"""

练习2 ： 拷贝一个目录
编写程序完成，将一个文件夹拷贝一份
* 假设文件夹中只有普通文件
* 将每个文件的拷贝作为一个拷贝事件
* 使用进程池完成事件

提示 ： os.mkdir('name')

在拷贝的过程中实时显示拷贝内容的百分比

提示： 文件夹的 = 所有文件大小之和


"""
# from multiprocessing import Pool,Queue
# import os,sys
#


# q = Queue() # 创建消息队列
#


# # 拷贝一个文件
# def copy(file,old_folder,new_folder):
#     fr = open(old_folder+'/'+file,'rb')
#     fw = open(new_folder+'/'+file,'wb')
#     while True:
#         data = fr.read(1024)
#         if not data:
#             break
#         n = fw.write(data) # write的返回值就是写入的字符数，所以写入多少就是拷贝多少
#         q.put(n) # 放入消息队列
#     fr.close()
#     fw.close()
#



# # 获取文件夹大小
# def get_size(dir):
#     total_size = 0
#     for file in os.listdir(dir):
#         total_size += os.path.getsize(dir+'/'+file)
#     return total_size
#


# # 使用进程池
# def main():
#     old_folder = input("你要拷贝的目录:")
#     # 文件夹大小
#     total_size = get_size(old_folder)
#     new_folder = old_folder + "-备份"
#     try:
#         os.mkdir(new_folder)
#     except:
#         sys.exit("该目录已存在")
#
#     # 创建进程池
#     pool = Pool()
#
#     # 遍历目录，确定要拷贝的文件
#     for file in os.listdir(old_folder):
#         pool.apply_async(func=copy,args=(file,old_folder,new_folder))
#
#     copy_size = 0
#     while copy_size < total_size:
#         copy_size += q.get() # 从消息队列获取数值累加
#         print("拷贝了 %.2f%%"%(copy_size/total_size*100))
#
#
#     pool.close()
#     pool.join()
#



# if __name__ == '__main__':
#     main()
#















'''

#### 2.2.5 进程通信

* 必要性： 
    进程间空间独立，资源不共享，此时在需要进程间数据传输时,就需要特定的手段进行数据通信。

* 常用进程间通信方法：
    消息队列；
    套接字:【例如一个子进程负责接受消息，父进程负责发送消息，则父进程自己给自己的套接字地址发送消息的话，就被子进程收到了】

* 消息队列使用
  * 通信原理：
            在内存中开辟空间，建立队列模型，进程通过队列,将消息存入，
                                        或者从队列取出,完成进程间通信。
                                      
  * 实现方法
  
  from multiprocessing import Queue

  q = Queue(maxsize=0)
  功能: 创建队列对象
  参数：最多存放消息个数,【不写的话，则系统自定义】
  返回值：队列对象

  q.put(data,[block,timeout])
  功能： 向队列存入消息
  参数： data     要存入的内容                      【字符串、列表等所有数据类型】
  	    block    设置是否阻塞 False为非阻塞         【默认是阻塞，即队列满的时候，put的时候会等待】
  	    timeout  超时检测                         【阻塞的时候，最多等多长时间】

  q.get([block,timeout])
  功能：从队列取出消息
  参数：block       设置是否阻塞 False为非阻塞【默认是阻塞，即队列为空的时候，会等待】
  	   timeout     超时检测【阻塞的时候，最多等多长时间】
  返回值：          返回获取到的内容

  q.full()   判断队列是否为满
  q.empty()  判断队列是否为空
  q.qsize()  获取队列中消息个数
  q.close()  关闭队列，即销毁队列



'''

"""
进程间通信
"""
#
# from multiprocessing import Process,Queue
#
# # 创建消息队列【必须在父进程里创建队列，子进程使用队列】
# q = Queue()
#
# # 定义子进程的函数，对应两个子进程
# # 一个函数向队列里写消息，一个函数向队列里读消息
# def request():
#     name = "Levi"
#     passwd = "123"
#     # 存入消息队列
#     q.put(name)
#     q.put(passwd)
#
# def handle():
#     # 获取消息队列内容
#     name = q.get()     #先put到队列里的消息，先被get出来       #每次get，只能get到一个消息
#     passwd = q.get()
#     print("用户:",name)
#     print("密码:",passwd)
#
#
# #创建子进程、执行函数
# p1 = Process(target = request)
# p2 = Process(target = handle)
#
# p1.start()
# p2.start()
#
# #阻塞、等待，回收子进程
# p1.join()
# p2.join()
#






















'''
**群聊聊天室 **

> 功能 ： 类似qq群功能
>
> 【1】 有人进入聊天室需要输入姓名，姓名不能重复
>
> 【2】 有人进入聊天室时，其他人会收到通知：xxx 进入了聊天室
>
> 【3】 一个人发消息，其他人会收到：xxx ： xxxxxxxxxxx
>
> 【4】 有人退出聊天室，则其他人也会收到通知:xxx退出了聊天室
>
> 【5】 扩展功能：服务器可以向所有用户发送公告:管理员消息： xxxxxxxxx
>
>
'''

