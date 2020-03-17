#module

#知识概括：
#A.那么什么是module呢，有什么用呢？
  #a.作用：我们希望代码可以重复使用
  #b.对module的定义：
# In this lesson, we’ll explore how to use tools other people have built in Python
# that are not included automatically for you when you install Python.
# Python allows us to package code into files or sets of files called modules.

  #c.package又是什么？一个package里面包含了多个modules。

  #d.如何import的基本语法
# first way:
# import module_name
# module_name.function  --> 第一种方法和后面两种的区别是，在funcion前面还要加上module_name.

#second way:
# from module_name import function --> 这样语法格式的直接用function_name 就可以了，不需要在前面再加上module的名字。
# function()

#third way
# from module_name import *  --> 直接import了整个module里的所有function
# function()

#1.module的基本介绍，和使用示例。
from datetime import datetime
current_time = datetime.now()
print(current_time)

#2. random这个module

# Import random below:
import random
# Create random_list below:
random_list = []
# Create randomer_number below:生成一个list，这个list里面有100个数，而且这每一个数，都是从0到100随机产生的。
for i in range(101):
  result = random.randint(1,100) #这个包含1和100的，不用考虑什么上限。下限的问题。
  random_list.append(result)
print(random_list)
# Print randomer_number below: 从这个list随机选择一个element
randomer_number = random.choice(random_list)
print("the number is " + str(randomer_number))

#3.Modules Python Namespaces 给我们导入的命名

#In python, the 'as' keyword can be used to give an alternative name as an alias for a python module or function.

#when we use randint(), 我们就会使用 random.randint(),这个random是系统给我们默认提供的一个名称，
#我们导入了random这个module，python就会自动命名一个模块，叫random，但我们有时候不喜欢这个名字，我们想换一个名字。
#所以这时，我们就有了公式， import module_name as name_you_pick_for_the_module

#random.sample(range(x),y)
  #这个method的作用，比如下面的这个，会打出y个，在0和x之间的随机数字。
#理解这个range()的真正作用是啥。The range() function returns a sequence of numbers,
  #starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# import random as ran #导入了这个module。并且给这个module起了一个新名字叫作ran
# number1 = ran.sample(range(1000),100)
# print(number1)

from random import sample #从random这个module里只导入了sample
number2 = sample(range(1000),10)
print(number2)

from math import * #从math这个module里面导入了所有的
# import math
number3 = cos(90)
print("number3 is " + str(number3))
#看上去差不多，但在语法的使用上，还是有去别的。

#4.Module里面 不仅有function还有 data type,
from decimal import Decimal # 引入了decimal这个module里的一种数据类型 Decimal

cost_of_gum = Decimal('0.10')
cost_of_gumdrop = Decimal('0.35')

cost_of_transaction = cost_of_gum + cost_of_gumdrop

#5.modules python files and scope. 
#如果你想用别的文件中的 variable 或者 method，你同样需要 import，把它们导入之后，你才可以使用。
#注意：在import别的文件的时候，是不需要加后缀的。


#6.datetime
from datetime import datetime #左边的datetime是 module，只import datetime这个module里的datetime section，
print(datetime.now())


#7. pip
#什么是pip?
#因为python这个软件，或者library都有各种各样不同的版本，就很麻烦，所以现在就需要一个虚拟的环境，来运行python。
