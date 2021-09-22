class IterableHelper:

    @staticmethod     ##类里的静态方法，如果一个函数不需要调用类变量和实例变量，则可以定义成静态方法，
                      ## 通过类名点方法名调用，并且括号里没有self，
    def find(iterable, func):
        for item in iterable:
            if func(item):
                yield item

    @staticmethod
    def delete(list_targe,func):
        for i in range(len(list_targe) - 1, -1, -1):
            if func(list_targe[i]):
                del list_targe[i]

    @staticmethod
    def max(list_target, func):
        max = list_target[0]
        for i in range(1, len(list_target)):
            if func(max) < func(list_target[i]):
                max = list_target[i]
        return max

    @staticmethod
    def ascending_order(list_target,func):
        for i in range(len(list_target) - 1):
            for c in range(i + 1, len(list_target)):
                if func(list_target[i]) > func(list_target[c]):
                    list_target[i], list_target[c] = list_target[c], list_target[i]