#本节说的就是 class，obj

#1. We can check the type of a python variable using the type() function.
# 现在知道了data type 就是 class的意思
# type() returns the actual class an object is an implementation of.
test_sting = "Hello, my friend!"
test_int = 100 #现在我们知道，100（或者说test_int)就是一种obj，只要使用type这个function，就可以知道这个obj属于那个class

print(type(test_sting)) # --> 得到的结果是: <class 'str'>
print(type(test_int)) # --> 得到的结果是: <class 'int'>

#2.class, 什么是 class？

#A. 答：a class is a template模板 for a data type,
    #It describes the kinds of information that class will hold and how a programmer will interact with that data.

#B. 在python中 建一个class的格式如下所示：
class Myfirstclass:
    pass
    #注1：class_name 的首字母通常都要大写，（大家共同默认的潜规则）
    #注2：pass就是用来占位置的。

#3. instantiation实例化，class只是一个模板，我们要通过class建一个object
    #在上面，我们定义了一个class，这啥用也没有。
    #一个class必须要被实例化 --> we must create an instance of the class.

#如何 实例化 一个抽象的class呢？得像下面这样召唤一下
Myfirstclass_instance = Myfirstclass() #等号左边就是object的名称。
    #a class的instance, 我们常常叫它另一个名字，就是 object --> 这里讲到了我们所熟悉的 Objected Oriented Programming (OOP)

print(type(Myfirstclass_instance))
    #--> 打印出来的是 <class '__main__.Myfirstclass'>  ----> __main__.Myfirstclass
    #注：In Python __main__ means “this current file that we’re running”

#提醒：这个 type()是在干嘛？
    # Instantiation takes a class and turns it into an object,
    # the type() function does the opposite of that. When called with an object,
    # it returns the class that the object is an instance of.



#4.class variables （在后面我们还会介绍instance variables)
#   A.什么时候会用到这个 class variable呢？
#       when we want the same data to be available to every instance of a class.
#   B.如何给一个 class添加 class variable 呢？
#       很简单，直接在 class里写上这个 variable就好了，（但注意，不嫩写在任意一个method中）
#       题外话：我们也不可以在class中method外部，写一个类似于print()这样的动作，这样的动作只能在method中写。
#   C.那么如何访问这个 variable呢？
#   --> not that easy,
#   -->第一步：你要实例化这个class。第二步：使用这样的语法格式 object_name.variable_name


#下面进行展示：

#   新建一个class
class Astupid_class:
    a_stupid_variable = " hello, little bitch"  ####注意：class variable前面是不需要加self的，因为class variable和self没有关系！
#   实例化这个class
a_stupid_instance = Astupid_class()

#   使用这个 class variable
print(a_stupid_instance.a_stupid_variable)


#5.Method (method are defined as part of a class)
#第一部分介绍的是: Methods without arguments
#   创建一个 空的 class
class Myclass:
    variable1 = "1"

    def method1(self):
        print(self.variable1)
        #你往下面看，这个self.variable 指的就是 class_instance.variable1
        #!!!!!引用class variable，需要在variable前面加上self
        # 'self' refers to 'the object' calling the function.
        # 简单点说，self指的就是未来object的名字，但我们此时此刻不知道那个object的名字，只好用self来代替。

#把这个class实例化
class_instance = Myclass()

#使用这个 instance
class_instance.method1()

#第二部分, 介绍的是 methods with arguments
#定义一个 class
class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile #这个miles，是在这个method中的variable,所以在前面不需要加self
#把这个method实例化
converter = DistanceConverter()
#调用这个instance里的 method
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)

#6. Constructors 构造器

#英文版的介绍（没说到重点）
# There are several methods that we can define in a python class that have special behavior.
# These methods are sometimes called “magic”, because they behave differently from regular methods.
# Another popular term is dunder methods, so-named because they have two underscores (double-underscore abbreviated to “dunder”) on either side of them.

#中文版介绍
#A. 这一节我们主要介绍  __init__ 这个method

#   第一个功能：
#示范：创建一个class
class Shouter1:
    def __init__(self):
        print("Hello")
#实例化一个class
shout1 = Shouter1() #每次实例化这个class的时候，都会print一遍 "hello"

#   第二个功能：
#示例：再创建一个class
class Shouter2:
    def __init__(self, what_you_want_to_shout):
        print(what_you_want_to_shout)

#再实例化这个class --> 并且在实例化的时候，还接受一个argument！
shout2 = Shouter2("fuck you!")

#7. instance variables （要想有instance variable，必须先得到一个object，再利用obj的名字 往里面添加 新的variable)
#举例：
#先创建一个无关紧要的class
class One_class:
    pass

#实例化这个class，得到一个object1，然后，居然还给这个object1新添加了一个variable，这个variable的名字就叫instance_variable_1
object1 = One_class()
object1.instance_variable_1 = 100
print(object1.instance_variable_1)

#实例化这个class，得到一个object2，然后！居然还给这个object2新添加了一个variable，这个variable的名字就叫instance_variable_1
object2 = One_class()
object2.instance_variable_1 = 101
print(object2.instance_variable_1)


#8. 如何避免我们要使用的variable （其实并不存在）
    #instance variable 和 class variable --> they are both considered attributes of an object.
    #当我们尝试去使用一个variable, 但这个variable并不存在，这可咋办？ python will throw an AttributeError
    #所以，我们肯定要避免这个情况，于是，在这里，我们就学习到了两个新的function

#创建了一个class
class Class2:
    variable9 = 9
    variable8 = 8
    def func1(self):
        variable7 = 7

#实例化一个class
obj3 = Class2()

#土方法：我们一直使用的 try: except
try:
    print(obj3.variable7)
except AttributeError:
    print("we don't have this varibale in both class and object" )
#我试了variable7 和 6都会打印出这句话！ 这就很神奇了！ v7是在class的function里，居然也不能调用！

#新方法, 介绍两个

#第一个: hasattr(obj_name, variable_name)
print(hasattr(obj3,"variable5"))
#1. 左边是 object_name
#2. 右边是 Variable name，值得注意的是 variable name 要打上引号。
#3.如果有这个变量，返回的是true，如果没有，返回的是 false

#第二个: getattr(obj_name,variable_name,默认值）
print(getattr(obj3,"variable8",800)) #800 就是 the default value
    #如果有，返回的就是variable8的值
    #如果没有，返回的就是最后一个 default value
    #不要想太美，不是给你创建一个variab8，并且让它等于800，而是给你返回一个默认值，就是800

#一个非常有深度的例题：
    #如下所示， 告诉我们 无论是 int,string, dictionary 还是其他数据类型，都是class，每种class能干的事不一样。
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

#我想看看，这各个obj都有啥功能嘞。
for i in how_many_s:
    print(dir(i)) #在第二个和第四个，居然真的有 count 这个attribute，天哪，真的太神奇了！

for i in how_many_s:
  print(i)
  if hasattr(i,"count"): #有的话就可以继续执行下面的
    print("得到的结果是:" + str(i.count("s")))
    print("---------------------------------")
  else:
    print("很抱歉，这种object是没有count这个variable的，换句话说，这个object所属于的class是不支持计数的。")
    print("---------------------------------")

#9. self
class Expclass:
    #class 中的第一部分：变量
    variable1 = 1

    #class中的第二部分： __init__ 初始函数 --> 也可以叫他constructor
    def __init__(self,variable2):
        print(variable2)
            #在这个__init__里面使用variable2肯定是没问题的。
        self.variable2 = variable2
            #把输入进来的这个variable2 赋值给 self.variable2 --> 以后就拿着self.variable2 在这里使用
            #####上面这个步骤极为重要！！！！ 注意记忆!!! 这个是很有道理，而不是一句废话。

    #class 中的第三步部分，普通method
        #在另外一个method中，使用variable2
    def method_1(self): #只要与self挂钩的变量，括号里都不需要再写一遍了，有一个self就够了。
        print(self.variable2)#在这里，你想用上面输入进来的 variable2, 但你却不可以直接输入variable2, 必须使用的是 self.variable2


#进行实例化
obj1 = Expclass(2)

#开始使用
print(obj1.variable1) #在外面用到这个的时候，不能继续叫作self.variable1, 而得把这个self改成你创建的obj的名字。

#这样做的意义是，你可以创建很多很多obj（而这些obj储存的数据都是不相同的）
obj1.method_1()

#一个很好的例子
class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        # Add assignment for self.radius here:
        self.radius = diameter / 2

    def circumference(self):
        result = 2 * (self.pi) * (self.radius)
        return result


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

#10. 这一节我们学习的是 dir(),用这个, 可以查看一个object所对应的类 的所有属性 (类的属性 - class attribute)
#在一个网站上看到，类拥有两种操作，1.类属性，2.实例化
#类属性 就相当于一个类的变量（注意是相当，只是打个比方，并非真的是）。
#使用的方法是：　class_name.attribute_name


class Emptycalss:
    pass

obj_empty = Emptycalss()
obj_empty.i_create_a_varible = "99" #我在这里自己加了一个 varible，当我再打印下面的时候，就会发现attribute里面多了一个东西！神奇！
#怪不得前面的人说 attribute 就相当于一个 variable.
#但这些attribute和variable 的区别是，这些attribute是系统自带的。That’s certainly a lot more attributes than we defined! Python automatically adds a number of attributes to all objects that get created.
#These internal attributes are usually indicated by double-underscores. 这些自带的attributes前后都有两个_
print(dir(obj_empty))

#11. String Representation --> 这节我们学的是 __repr__

#你是不可以直接打印一个object的，如果你尝试打印的话，返回的将是一串你看不懂的数字，这段数字指的是 where the class is defined and
#our computer's memory address where this object is stored.

#创建一个class
class Myclass11:
    def __init__(self,variable1):
        self.variable1 = variable1 # 意思是把这个 variable1，assign到 self.variable1(每当你困惑的时候，就要想想这个等号是什么意思）

    def __repr__(self): #这个repr只能有一个self
        return self.variable1

#创建一个obj
obj11 = Myclass11("hello")#这个variable 必须是 string，而不能是其它的。

#但有了那个玩意，这个时候我们就可以! 使用 print了！ 哈哈哈
print(obj11)



#11. 总结
#what a data type actually is in python？
    # 一个int，一个string， 都可以是一个object。
    #也可以我们自己创建一个class，然生生成一个object。
    #我们还可以用 dir(object_name) 来查看这个obj所属class的属性。
    #we learned how to create our own data types using class keyword.
#知道了 class 与obj的关系
    #从class创建一个obj
    #知道这个obj是属于哪个class的，就使用type()
#https://www.codecademy.com/learn/paths/computer-science/tracks/cspath-python-objects/modules/cspath-python-classes/cheatsheet
#复习提纲如上
#the first argument of a method: the instance of the object itself, we usually refer it as self. 

class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if type(grade) is Grade: ##这句话是这道题的关键，检查这个obj是不是这个class的obj，用这个指令就好
            (self.grades).append(grade)


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)


class Grade:
    minimum_passing = 65  # 为啥不要加self，仔细想想就知道,因为这是class variable，无论你怎么创建obj，都会是这样。
    def __init__(self, score):
        self.score = score

#初始化了grade
grade1 = Grade(100)


#给stundent这个obj里面 添加grade1
pieter.add_grade(grade1)
print(pieter.grades) #令人无奈的是：最后打印出来的依然还是 object的一串乱码



