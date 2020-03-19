"""
Overview
in this lesson, we learned:
    How to create a subclass of an existing class.
    How to redefine existing methods of a parent class in a subclass by overriding them.
    How to leverage a parent class’s methods in the body of a subclass method using the super() function.
    How to define a Python exception that inherits from Exception.
    How to write programs that are flexible using interfaces and polymorphism.
    How to write data types that look and feel like native data types with dunder methods.

cheatsheet:
https://www.codecademy.com/learn/paths/computer-science/tracks/cspath-python-objects/modules/cspath-python-classes/cheatsheet
"""

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

#3. Overriding Methods 覆盖方法（
#在前面两部分， 子类继承 父类， 子类只是更改了父类的一些variable，于是，问题来了，如果子类想更改父类的method，那该咋办？

#一个很好的例子：

#首先，创建一个class
class Message:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text

#从Message这个class中得到一个 obj叫作 message1
message1 = Message("haiyang", "yena", "hello")

#再创建，一个class，并且，这是一个 父类。
class User:
    def __init__(self, username): #再创建obj的时候，就需要输入。
        self.username = username

    def edit_message(self, message, new_text):  #在调用这个method的时候，才需要输入这些。
        #在这里令我惊讶的是，一个obj也可以被当成argument输入进来。
        if message.sender == self.username:
            message.text = new_text


user1 = User("haiyang") #从上面这个class中 创建了一个 obj
user1.edit_message(message1, "fuck you")


class Admin(User): ##############
    def edit_message(self, message, new_text):###############
        message.text = new_text ##############这一节的重点在这，复写这个 method，就是这样？！ very easy！

user2 = User("anyone")#上面要求必须是haiyang，就是发这条信息的人，但在这里，所有人都可以。
user2.edit_message(message1,"hello baby")


#4. super()
#上面，我们介绍了如何 复写整个method，

#这里和上面的不同是，并不用复写整个method，在获取父类某一method全部的基础上，在子类中，还可以对这个method进行修改。

class Base_class1:
    def __init__(self,arg1,arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def method_i_create(self,arg4,arg5):
        print(arg4)
        print(arg5)

class Sub_class(Base_class1):
    def __init__(self,arg1,arg2,arg3):
        self.arg3 = arg3
        super().__init__(arg1,arg2) #这个和下面的一样，就是在召唤父类里的那个method而已，没有啥不一样的地方

    def method_i_create2(self,arg6,arg7,arg8):
        super().method_i_create(arg6,arg7) #我认为 super() 指的就是父类某不知名的object而已。
        print(arg8)

##第一个试验
sub_obj1 = Sub_class(1,2,3)#在原有的基础上，新增加了一个3。1和2都是从Base class那里继承来的。
print(sub_obj1.arg1)
print((sub_obj1.arg2))
print(sub_obj1.arg3)

#第二个试验
sub_obj1.method_i_create2(6,7,8) #新增加了一个8。6和7都是从Base class那里继承来的。

#小插曲：介绍一下None
#None 在python中就相当于false，所以如果None出现在if后面，那么if下面的语句都不会被执行。
if None:
    Print("hoi")
if (not None):
    print("hi")


#5.Interfaces 接口
# when two classes have the 'same method names' and 'attributes'(在class中，class variable还有个名字就是attributes)
# we say they implement 'the same interface'.

#interface的中文定义， 当两个class中的 attributes 和 method name是一样的时候，我们就说他们有一样的接口。

class InsurancePolicy: #这个就是父类
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item


class VehicleInsurance(InsurancePolicy):  # 创建了一个子类, 创建子类的时候，就等于把父类的所有东西，照单全收了
#在这个子类里面虽然看不见，但父类上面的全部内容，其实都是在这里的。你只要假装父类的东西在这里就好了。
    # def __init__(self, price_of_item):
    #     self.price_of_insured_item = price_of_item
    def get_rate(self):
        result = 0.001 * self.price_of_insured_item
        return result

class HomeInsurance(InsurancePolicy):  # 又创建了一个子类
    def get_rate(self):
        result = 0.00005 * self.price_of_insured_item
        return result

object1 = VehicleInsurance(1000)#子类里面并没有写 __init__ 但为啥在创建obj的时候，需要输入1000呢？因为它继承了父类啊
object2 = HomeInsurance(500) #这栋房子值500元


#6.polymorphism 多态性

#多态性的定义： Polymorphism is the term used to describe the same syntax doing different actions depending on the type of data.
#相同的syntax，对于不同的数据类型，会出现不同的行为.

# + 加号是最好的例子
# For an int and an int, + returns an int
2 + 4 == 6

# For a float and a float, + returns a float
3.1 + 2.1 == 5.2

# For a string and a string, + returns a string
"Is this " + "addition?" == "Is this addition?"

# For a list and a list, + returns a list
[1, 2] + [3, 4] == [1, 2, 3, 4]


#7.Dunder Methods (在class中，前后又两根_ 的方法）
#前面我们已经学过两个了。

#这一节并不是想再教给我们一个新的，而是想告诉我们:
# python gives us the power to define dunder method that define a custom_made class to look and behave like a Python builtin.

#下面演示 如何 获得一个 个性化定制的 Dunder method

#先用古老的，不方便的方法展示：
class Color:
    def __init__(self,red,blue,green):
        self.red = red
        self.blue = blue
        self.green = green

    def __repr__(self): #以后创建了obj，如果你使用打印obj，就会打印出这个东西，指的就是这个obj represent什么东西。
        return "Color with RGB = ( {} , {}, {} )".format(self.red,self.blue,self.green)

    def add(self, other): #这个method实在是让我搞不懂，居然可以把自己所在class的object当作输入(other就用来接受另一个obj)。
        #adds two RGB colors together
        new_red = min(self.red + other.red , 255) #最大值只能是255，用这个min是想确保最大值不能超过255
        new_blue = min(self.blue + other.blue , 255)
        new_green = min(self.green + other.green, 255)

        result = Color(new_red,new_green,new_blue) #卧槽，牛逼，在这里又生成了一个新的obj
        return result

    #获得一个obj，这个obj指红色
red = Color(255,0,0)

    #再获得一个obj，这个obj指蓝色
blue = Color(0,255,0)

    #调用这个add method，还可以生成一个 color (在这里 self指的是 red，other指的是blue）
new_color = red.add(blue)
print(new_color) ##用上了之前的那个 __repr__

#用本节提倡的先进方法进行展示：

class Color:
    def __init__(self,red,blue,green):
        self.red = red
        self.blue = blue
        self.green = green

    def __repr__(self): #以后创建了obj，如果你使用打印obj，就会打印出这个东西，指的就是这个obj represent什么东西。
        return "Color with RGB = ( {} , {}, {} )".format(self.red,self.blue,self.green)

    def __add__(self,other):  #等下使用的时候，直接用加号就可以了！
        new_red = min(self.red + other.red, 255)
        new_blue = min(self.blue + other.blue, 255)
        new_green = min(self.green + other.green, 255)

        result = Color(new_red,new_blue,new_green)
        return result

#得到三个obj
red = Color(255,0,0)
blue = Color(0,255,0)
green = Color(0,0,255)

#然后我们可以直接把这两个 obj 加载一起。

new_color_megenta = red + blue
print(new_color_megenta)

new_color_cyan = blue + green
print(new_color_cyan)

new_color_white = (red + blue) + green
print(new_color_white)


#这个没看懂
# In script.py there are two classes defined, Atom and Molecule.
# Give Atom a .__add__(self, other) method that returns a Molecule with the two Atoms together in a list.
class Atom:
    def __init__(self, label):
        self.label = label

    def __add__(self, other):
        return Molecule([self, other])


class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms


sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])


#Dunder methods II

#小插曲，先介绍一下 几个小function
x = iter (["apple","banana","orange"]) #对待list，可以这样用
print(next(x))
print(next(x))

y = {"first":1 , "second":2}#对待字典，可以这样用，这样刚好证明了，我们上面所说的多态性
z = iter(y)
print(next(z))
print(next(z))


#在这里，用我自己编写的例子，来仔细的解释这个概念

class Testclass:
    def __init__(self,arg1,arg2):
        self.list1 = arg1
        self.string2 = arg2

    def __iter__(self):
        result1 = iter(self.list1)
        return result1

    def __len__(self):
        result2 = len(self.list1) #测测这个list有多长
        return result2

    def __contains__(self,string3):
        result3 = string3 in self.list1 #如果在，返回的就是True，如果不在，返回的就是False
        return result3

    def __add__(self,string4): #这个例子要好好看看，真的太牛逼了！
        result4 = (self.string2 + string4).upper()
        return result4


test_obj = Testclass(["haiyang","jiang","yena","baby"],"hi")

# for i in test_obj.list1:
#     print(i)
# 去除掉上面的 __iter__就得写成这样了。

for i in test_obj: #__iter__在这个外面的形式就是 for x in obj_name
    print(i)
print(len(test_obj)) #输出的结果就是4
print( "yena" in test_obj ) #输出的结果是true --> 这个contains 在这里 用的是 'xx in xx_list'

print(test_obj + " my friend")



#在结尾做一个mini project，这个小例题讲的不错，很有深度的告诉了我们， 继承一个list，然后复写它的method是啥样的。
class SortedList(list):
  def append(self, value): #因为以后都是 self.append()
    super().append(value)
    self.sort() #这里为啥用self -看上面的comment就知道了， 因为这是一个从list继承来的 class，这里创造的obj其实都是 list，所以这个self指的就是list！

list1 = SortedList()
print(list1)

list1.append(100)
list1.append(76)
list1.append(23)
print(list1)