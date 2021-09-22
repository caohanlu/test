'''

* 什么是线程
  【1】 线程被称为轻量级的进程，也是多任务编程方式【各自执行，互不影响】
  【2】 也可以利用计算机的多cpu资源
  【3】 线程可以理解为进程中再开辟的分支任务

* 线程特征
  【1】 一个进程中可以包含多个线程
  【2】 线程也是一个运行行为，消耗计算机资源
  【3】 一个进程中的所有线程共享这个进程的资源
  【4】 多个线程之间的运行同样互不影响各自运行
  【5】 线程的创建和销毁消耗资源远小于进程

* 如果进程中没有创建线程，则叫做单线程编程



 2.3.2 多线程编程

* 线程模块： threading
* 创建方法
   【1】 创建线程对象
    from threading import Thread
    t = Thread()
    功能：创建线程对象
    参数：target 绑定线程函数【提前把线程要做的事，封装为函数】
         args   元组 给线程函数位置传参
         kwargs 字典 给线程函数键值传参

    【2】 启动线程
     t.start()

    【3】 回收线程，【线程没有僵尸的概念，即使不回收，系统也会在线程执行完成后，资源不够的时候，自动回收】
     t.join([timeout])

'''






"""
线程创建示例
无参数
"""
#
# import threading
# from time import sleep
# import os
#
# a = 1
#
# # 线程函数
# def music():
#     for i in range(3):
#         sleep(2)
#         print(os.getpid(),"播放:大花轿")
#     global a
#     print("a = ",a)   #1
#     a = 10000         #分支线程里修改全局变量a，主线程里也会受影响，变成10000，因为主线程和分支线程，使用的是相同的资源
#                       #这点跟父进程、子进程不一样，子进程修改全局变量，父进程不受影响
#
# # 创建线程对象
# # 【函数名不加括号，因为传递的是函数名，而不是执行函数】
# t = threading.Thread(target=music)
#
# # 启动线程，执行函数内容
# t.start()
#
# #主线程【父进程】执行的内容，【此时两个任务同时执行，抢占cpu时间】
# for i in range(4):
#     sleep(1)
#     print(os.getpid(),"播放:葫芦娃")   #主线程跟线程的pid，是一样的，因为主线程，包含了线程
#
#
# #  回收线程
# # 【阻塞、等待线程执行完成后，释放线程占用的父进程资源，这里的父进程，指的是这个程序一启动，就成了父进程】
# # 【一个进程里的多个线程，并发还是并行，也是操作系统决定的，可能占用一个cpu，也可能占用多个cpu】
# t.join()
#
#
# print("全局a:",a)   #10000








"""
循环、创建多个线程

函数有参数

"""
# from threading import Thread
# from time import sleep
#
# # 含有参数的线程函数
# def fun(sec,name):
#     print("含有参数的线程")
#     sleep(sec)
#     print("%s 线程执行完毕"%name)
#
# # 循环创建多个线程
# jobs = []
# for i in range(5):
#     t = Thread(target=fun,args = (2,),kwargs={"name":"T%d"%i})  #参数因为是元组，所以要有逗号
#     jobs.append(t)   #线程对象，追加到列表，后面统一join回收
#     t.start()        #for循环执行很快，所以可以看成五个线程，同时启动，抢占cpu时间
#
# # 回收线程
# [x.join() for x in jobs]
#







'''
* 线程对象属性
  * t.setName()  设置线程名称
  * t.getName()  获取线程名称【默认是Thread-1   Thread-2等】
  
  * t.is_alive()  查看线程是否在生命周期【没有执行完的话，就在生命周期】
  
  * t.setDaemon()  设置daemon属性值
  * t.isDaemon()  查看daemon属性值
  * daemon为True时，主线程退出分支线程也退出。
    要在start前设置，通常不和join一起使用。
    这个属性默认没设置

'''
"""
线程对象属性
"""
# from threading import Thread
# from time import sleep
#
# def fun():
#     sleep(1)
#     print("线程属性测试")
#
# t = Thread(target=fun)
#
# t.setDaemon(True)       # start前设置，这个线程随主线程的退出而退出
#
# t.start()
#
# print("Name:",t.getName())
# t.setName("tarena")     #设置线程名称
# print("Name:",t.getName())
#
# print("is alive:",t.is_alive())







'''

练习1： 模拟售票系统
现有500 张票 记为 T1--T500   放在一个列表
创建10个线程 模拟10个窗口，记为 w1 -- w10,每张票卖出需要0.1秒,票的售出顺序必须是1--500
每张票卖出时 打印  w2----T203

编程创建10个 线程模拟这个过程

'''
# from threading import Thread
# from time import sleep
#
# # 存储票【所有线程使用同一个列表。进程是做不到的，因为不同的进程，使用的是自己内存里的列表】
# ticket = ["T%d" % x for x in range(1, 501)]
#
# # 模拟每个窗口的买票情况 w 窗口编号
# def sell(w):
#     while ticket:                               #每个线程都执行这个函数，循环售票，直到列表为空，即没票了
#         print("%s --- %s"%(w,ticket.pop(0)))    #pop()删除列表最后一个元素，pop(0)删除列表第0个元素，返回值就是被删除的元素，
#         sleep(0.1)                              #sleep放后面，如果在pop前面，则有可能列表只有2个元素，但10个线程一起进入循环来pop，
#                                                 #则还有8个线程是pop不到数据的，会报错
#
#
# jobs = []
# for i in range(1,11):
#     t = Thread(target=sell,args=("w%d"%i,))
#     jobs.append(t)
#     t.start()
#
# [i.join() for i in jobs] # 回收
#







'''
自定义类来创建线程

1. 创建步骤
   【1】 继承Thread类
   【2】 重写`__init__`方法添加自己的属性，使用super()加载父类属性
   【3】 重写run()方法
2. 使用方法
   【1】 实例化对象
   【2】 调用start自动执行run方法
   【3】 调用join回收线程
'''

"""
自定义线程类演示
"""
# from threading import Thread
# import time
#
# class MyThread(Thread):
#     def __init__(self,song):
#         self.song = song   # 可以自定义一些属性
#         super().__init__() # 必须加载父类属性，即执行父类init函数来创建线程
#
#     def run(self):
#         for i in range(3):
#             print("Playing %s:%s"%(self.song,time.ctime()))
#             time.sleep(2)
#
# t = MyThread("小幸运")
# t.start()             # 执行run函数，即线程的工作内容
# t.join()









'''
 2.3.4 线程同步互斥

* 线程通信方法： 同一个进程的多个线程间，使用全局变量进行通信
             【而不同的进程之间通信，使用消息队列或者网络套接字】

* 共享资源争夺
  * 共享资源：多个进程或者线程都可以操作的资源称为共享资源。
            对共享资源的操作代码段称为临界区。
  * 影响 ： 对共享资源的无序操作可能会带来数据的混乱，或者操作错误。
           此时往往需要同步互斥机制协调操作顺序。


* 同步互斥机制【解决共享资源争夺问题】
  * 同步 ： 同步是一种协作关系，为完成操作，多进程或者线程间形成一种协调，按照必要的步骤有序执行操作。
               例如网络套接字里，客户端发消息，服务端收消息，如果收不到，则一直阻塞等待
               例如进程间通信的消息队列，队列满的时候，还往里put，则阻塞等待，
                                    队列空的时候，还get，则阻塞等待
  * 互斥 ： 互斥是一种制约关系，当一个进程或者线程占有资源时，会进行加锁处理，
           此时其他进程线程就无法操作该资源【即阻塞等待】，直到解锁后才能操作。
'''




'''
同步互斥第一种方法：

* 线程Event,线程事件

from threading import Event

e = Event()         创建线程event对象e

e.wait([timeout])   e阻塞等待，直到e被set，就结束阻塞  【参数是阻塞几秒，到时间后就结束阻塞。没参数表示一直阻塞】
e.set()             设置e，使e结束阻塞  【e.set()后，再调用wait，也不会阻塞】

e.clear()           使e回到未被设置状态  【e.clear()后，再调用wait，就会阻塞】
e.is_set()          查看当前e是否被设置  【true就不会被wait阻塞，false就会被wait阻塞】
'''

"""
event 线程同步互斥演示
"""

# from threading import Thread,Event
#
# msg = None  # 线程间通信
# e = Event() # 创建event对象
#
# def 杨子荣():                      #线程，修改全局变量msg
#     print("杨子荣前来拜山头")
#     global msg
#     msg = "天王盖地虎"
#     e.set()                       #线程修改完全局变量后，取消阻塞，则主线程开始执行
#
# t = Thread(target=杨子荣)
# t.start()
#
# # 主线程中认证                    #主线程，判断全局变量msg，是否被线程，修改成主线程想要的值
# print("说对口令才是自己人")
# e.wait()                       # 涉及到对全局变量msg的判断时，阻塞主线程，等待线程修改全局变量
# if msg == "天王盖地虎":
#     print("宝塔镇河妖")
#     print("确认过眼神，你是对的人")
# else:
#     print("打死他.....无情啊.....")
#
#
# t.join()






'''
同步互斥第二种方法：

* 线程锁 Lock
from  threading import Lock
lock = Lock()  创建锁对象
lock.acquire() 锁对象上锁,【如果锁对象lock已经上锁,再调用acquire会阻塞】
lock.release() 锁对象解锁,【解锁后，锁对象才可以再上锁】

上锁、解锁，也可以如下，功能跟上面写法一样：
with  lock:  上锁
...
...
	 with代码块结束自动解锁


'''

"""
线程同步互斥 Lock方法
"""

# from threading import Thread, Lock
#
# lock = Lock()  # 创建一个锁对象
#
# # 全局变量，即线程的共享资源
# a = b = 0
#
#
# def value():
#     while True:
#         lock.acquire()  # 上锁  #线程执行的时候，上锁，主线程无法执行，直到线程解锁
#         if a != b:
#             print("a = %d,b = %d" % (a, b))
#         lock.release()  # 解锁
#
#
# t = Thread(target=value)
# t.start()
#
# while True:
#     with lock:  # 上锁    #主线程执行的时候，上锁，线程无法执行，直到主线程解锁
#         a += 1
#         b += 1
#         # 语句块结束自动解锁
#
# t.join()


"""
练习1：  一个线程打印1--52  另一个线程打印A--Z
        两个线程一起启动，要求打印的结果
        12A34B56C.....5152Z

        提示: 使用同步互斥方法控制线程执行
             程序中不一定只有一个锁，这里可以创建两个锁对象
"""
# from threading import Thread, Lock
#
# lock1 = Lock()
# lock2 = Lock()
#
#
# def print_num():
#     # 每次循环打印2个数字
#     for i in range(1, 53, 2):
#         lock1.acquire()
#         print(i)
#         print(i + 1)
#         lock2.release()
#
#
# def print_char():
#     for i in range(65, 91):   #打印字母
#         lock2.acquire()
#         print(chr(i))
#         lock1.release()
#
#
# t1 = Thread(target=print_num)
# t2 = Thread(target=print_char)
#
# lock2.acquire()  # 让数字先执行
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()






'''
#### 2.3.5 死锁
* 什么是死锁
  死锁是指两个或两个以上的线程在执行过程中，由于竞争资源或者由于彼此通信,而造成的一种阻塞的现象，
  若无外力作用，它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁。

* 死锁产生条件
  * 互斥条件：指线程使用了互斥方法，使用一个资源时其他线程无法使用。
  * 请求和保持条件：指线程已经保持至少一个资源，但又提出了新的资源请求，在获取到新的资源前不会释放自己保持的资源。
  * 不剥夺条件：不会受到线程外部的干扰，如系统强制终止线程等。
  * 环路等待条件：指在发生死锁时，必然存在一个线程——资源的环形链，
               如 线程T0正在等待一个T1占用的资源；T1正在等待T2占用的资源，……，Tn正在等待已被T0占用的资源。

* 如何避免死锁
  * 逻辑清晰，不要同时出现上述死锁产生的四个条件
  * 通过测试工程师进行死锁检测

'''







'''
#### 2.3.6 GIL问题
* 什么是GIL问题 （全局解释器锁）
  由于python解释器设计中加入了解释器锁，导致python解释器同一时刻只能解释执行一个线程，大大降低了线程的执行效率。
  【即多个线程，虽然使用了多个cpu，但是多个线程无法同时执行】

* 导致后果
  因为遇到阻塞时线程会主动让出解释器，去解释其他线程。
  所以python多线程，在执行，多阻塞任务时，可以提升程序效率，
  如果没阻塞，则并不能对效率有所提升。

* GIL问题建议
    * 尽量使用进程，完成无阻塞的并发行为
    * 不使用c作为解释器 （Java  C#）
     Guido的声明：<http://www.artima.com/forums/flat.jsp?forum=106&thread=214235>

* 结论 
  * GIL问题与Python语言本身并没什么关系，属于解释器设计的历史问题。
  * 在无阻塞状态下，多线程执行效率并不高，甚至还不如单线程效率。
  * Python多线程，只适用于执行，有阻塞延迟的任务情形。
  
'''









'''

#### 2.3.7 进程线程的区别联系

* 区别联系
1. 两者都是多任务编程方式，都能使用计算机多核资源
2. 进程的创建/删除,消耗的计算机资源比线程多
3. 进程空间独立，数据互不干扰，有专门通信方法；
    线程使用全局变量通信
4. 一个进程可以有多个分支线程，两者有包含关系
5. 多个线程共享进程资源，在共享资源操作时往往需要同步互斥处理
6. Python线程存在GIL问题，但是进程没有。

* 使用场景
1. 任务场景：一个大型服务，往往包含多个独立的任务模块，每个任务模块又有多个小独立任务构成，
            此时整个项目可能有多个进程，每个进程又有多个线程。
2. 编程语言：Java,C#之类的编程语言，在执行多任务时，一般都是用，线程完成，因为线程资源消耗少；
            而Python由于GIL问题往往使用多进程。
            
            
'''


