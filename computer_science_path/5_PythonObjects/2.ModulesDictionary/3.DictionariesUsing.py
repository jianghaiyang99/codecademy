#本节内容大概：
    # Use a key to get a value from a dictionary, 使用key来查看一个dictionary里的value
    # Check for existence of keys 检查这个key存不存在于这个字典
    # Find the length of a dictionary 查看这个字典有多长
    # Iterate through keys and values in dictionaries 遍历字典中的键和值

#1.使用key来查看一个dictionary里的value
    #dictionary_name["value_name"] -->可以查询到那个value, 这不就是在把字典当作list来使用么。
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
print( building_heights["Burj Khalifa"] )

#2.check if the key exists in the dictionary.
# 第一种方法：语法格式 key_name in list_value -->通常用在if后面，会返回true 或者 false
my_room = {"boy":"haiyang jiang","girl":"yena shan"}
if "boy" in my_room:  #-->  "boy" in my_room --> 如果boy这个key在 my_room这个字典里的话，这个语句返回的值就是ture，所以下面的代码就
    #会被执行
    print("yes, this key is in the dictionary.")

#第二种方法，来检测这个key 在不在， Try/Except to get a key --> 用以前学的 try 和 except
key_to_check = "Landmark 81"
try:
  print(building_heights[key_to_check]) #就是要执行的代码而已，故作悬疑!
except KeyError: #except右边的是错误类型，常见的错误类型有： IndexError, KeyError, ValueErroe 等，这些error都是有自己名字的。
  print("That key doesn't exist!") #这个语句平时是不打印的，除非有了错误的时候（而且错误类型刚好就是 except旁边的），这个语句就会被执行。

#3.安全的方法获得一个key 和 value
    #safely get a key --> .get(key_name , "something you want to show if this value does not exist.")
    #为啥要用这个呢？ 因为，我们之前用的 my_dict[key]， 如果字典里面没有，那可坏事了，那这个代码就运行不了，因为有bug了。
    #所以在这个时候，我们就要使用 .get(), 如果我们要的key不存在与字典里的话，代码也不会有bug，只会返回一个none
my_room = {"boy":"haiyang jiang","girl":"yena shan"}
print(my_room.get("gay")) #这个打印出的结果就是none

     #还可以再升级一下，
print(my_room.get("gay","this key does not exist!")) #如果gay这个key不存在的话，就会打印出右边的值。

#4. delete a key , 删除这个字典中的一个 key --> .pop(a,b)先return这个key的value，然后再把这个key从字典里删除
    #使用的方式就是: .pop(key_value, "something you want to show if this value does not exist." )
    # 在你删除的时候，也有可能这个key本身就不存再，所以就需要逗号右边的那个东西，如果这个key不存在于字典里，就会return右边的这个值。
    #.pop()的作用不仅仅是删除，先return这个key的value后，再把这个key给删除了。

#5. get all 'keys'
# 有两种方法
    #第一种方法是：使用我们之前一直用的 list() --> list(dictionary_name) --> 就会把dictionary里面所有的key给打印出来。

    #第二种方法是：.key()
my_room = { "boy":"haiyang jiang" , "girl":"yena shan" }
out_put = my_room.keys()
print("使用了 .key() 之后，就会打印出这个：")
print(out_put) ##居然会生成一个 object，这个object就是dict_keys(我们这么称它）

#可以理解为 使用 .key() 生成了一个 list，于是，就可以用上循环，把list中的每一个元素都打印出来。
print("这两个是不是一样呢")
for i in my_room.keys():
    print(i)


#6. give all 'values'
    #和上面的 .key() 相对应，这个是 .value --> 同样是生成一个object，这个object包含了这个dictionary里所有的value
    #如何把这个obeject给转换成list --> 用我们之前学的 list() --> 这个function，专门就是把 object转换为 list

#7. give all 'items' -> 这个比上面的两个都要厉害，直接把这个字典里所有的东西都给打出来

    #用法一：
my_room = { "boy":"haiyang jiang" , "girl":"yena shan" }
result7 = my_room.items()
print(result7) #直接打印出来，是这样的，dict_items([('boy', 'haiyang jiang'), ('girl', 'yena shan')])

    #用法二：可以把它和 for循环结合起来，
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
for company, value in biggest_brands.items(): #左边的company 和 value还是随便起的名字（用于for循环）。
  print(company + " has a value of " + str(value) + " billion dollars. ")
