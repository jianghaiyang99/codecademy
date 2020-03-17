# Dictionary 字典

#1.问：什么是字典？ 答：就是用来储存信息的

#示例：menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

#格式细说：
# A dictionary begins and ends with curly braces ({ and }). 用大括号括起来
# Each item consists of a key (i.e., “oatmeal”) and a value (i.e., 3) 每一个item由key和value组成。
# Each ' key:value pair ' (i.e., "oatmeal": 3 or "avocado toast": 6) is separated by a comma (,) 每一对都由逗号分隔开。


#2. make a dictionary 如何创建一个字典？

#A.字典里可以放 任何你想放的东西，字典就像一个容器，放入所有你觉得有用的关系。
    #一个字典，甚至可以被当作是value，放入进另一个字典。
    #话虽这么说，但是对于key也是有要求的，--> key mush always be unchangeable, hashbale data types, like 'numbers' or 'strings'
        #children = {["Johannes", "Rosmarie", "Eleonore"]: "von Trapp", ["Sonny", "Fredo", "Michael"]: "Corleone"}
        #像这个，明显就是错误的。list放在value那里是可以的，但是放在key那里就不可以了！

#3.empty dictionary 创建一个空字典
empty_dictionary = {} #就是一个空的大括号

#4.给字典添加 新的内容 （添加一个）
animals_in_zoo = {}
animals_in_zoo["zebras"] = 8 #这个字典的语法格式和 list真的特别相似

#5.添加两个（add multiple keys) --> 这个时候就需要使用function，这个function就是 .update()
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper":138475,"stringQueen":85739}) #注：小括号中还有大括号！

#6.Overwrite Values
#注意：下面的字典里本来就有 "oatmeal": 3，然后再输入一遍，这个里面的数据就会被更新了。
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)

#7.把两条 list 变成一个 字典（没错，字典可以由两条长度一样的list组成！）
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {key:value for key,value in zip(names, heights)} #<--语法格式就是左边这样,注意 for后面跟的还必须是 key,value
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

#--------------------------------------------------------------------------------------
print(list(zip(names,heights))) #这仅仅是把两条list，变成了一条list而已，并不变成了一个字典。
# --> a zipped list of pairs between the drinks and caffeine.

#顺序一定要 对应好！

#8.cheat sheet for python,
# https://www.codecademy.com/learn/paths/computer-science/tracks/cspath-python-objects/modules/cspath-python-dictionaries/cheatsheet




