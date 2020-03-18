#1. Inheritance 继承

#what if we need a class that looks like a class we already have?

#Think of inheritance as a remix. it sounds a lot like the original, but there's something... different about it.
#继承，就是大部分和 爸爸是相同的，但是也有一定的区别

#创建一个 作为 base 的 class （英文名 叫作 base class）
class Base_class:
    am_I_stupid = False

    def __init__(self,username):
        self.username = username
#创建一个 作为 儿子的 class（ 英文名叫作 sub class)
class New_class(Base_class): #注意看这个语法格式，在创建class的时候，右边居然多了一个括号，括号里写的就是 父亲class的名字
    am_I_stupid = True #在这里，我们修改了父类的一些数据

#2. Exceptions 异常 （其实这一节，主要在帮助我们复习 继承的概念）

#首先，我们了解这个 built in function,
#issubclass() is a Python built-in function that takes two parameters.
#issubclass() returns True if the first argument is a subclass of the second argument.
#It returns False if the first class is not a subclass of the second

print(issubclass(ZeroDivisionError, Exception))

#由这上面的就可看出 An exception（指的就是ZeroDivisionError) is a class that inherits from python's Exception class.


class Exception_level2 (Exception): #这就是个异常，里面啥也没有，啥也不能写。
    pass #所以这个 Exception_level2 就继承了 Exception这个class的大多性质！！！

#首先，让我们来检查一下 Exception_level2 是不是 Exception的儿子。
print(issubclass(Exception_level2,Exception)) #显示的是True

class PositiveNumbers:
    def __init__(self,number):
        self.number = number

    def is_it_positive(self):#在class中，所有的method都是需要self的
        if self.number > 0:
            print("it is very ok !")
        else:
            raise Exception_level2

a_small_test = PositiveNumbers(2)#通过改变这里数字，来获得不同的结果。
a_small_test.is_it_positive()

