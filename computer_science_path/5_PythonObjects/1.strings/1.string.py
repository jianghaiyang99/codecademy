################Negative Indices
#其实这个和list还是一个道理，从后面往前选，倒数第一个肯定就是-1

my_name = "haiyang"

last_char = my_name[-1]
last_three_char = my_name[-3:]#我认为打印出来的分别是 倒数第三个，倒数第二个，和最后一个。
print(last_char)
print(last_three_char)

#####################Strings are immutable 一尘不变的Strings,
##什么意思？ string一旦被创建出来之后，就不可以再修改了，不懂就看下面的例子

test_string = "apple"
#test_string[0]= "b"
#解除上面这个的#，你会发现这个代码是错误的，因为string一旦被创建，就再也无法修改了。
print(test_string)

##############Escape Characters
#在string中，有时候，我们需要用到双引号，但是你不能直接插入，不然会有错误，这个时候该怎么办呢？
# 这个的秘诀就在于使用反斜杠
password = " theycallme\"crazy\"91"
print(password)

######Iterating through Strings
#String 其实就是一个list，所以 我们就可以用对 string用上for循环，和while 循环
to_be_printed = " i am your father"
def print_each_letter(word):
    for i in word:
        print(i)
print_each_letter(to_be_printed)

#用循环来制作一个function，这个function可以知道一个string里面有多少个字母
test1 = "what is your name? my name is your father"
def get_length(input_string):
    length = 0
    for i in input_string:
        length += 1
    return length

a = get_length(test1)
print(a)

###Strings and conditionals
#没啥稀奇的，就是把Strings在当 list用
my_name = "haiyang jiang"

#示例，在一个句子里，找到a
def how_many_a_in_this_string(input_string):
    counter = 0
    for i in input_string:
        if i == "a": #注意了！ 这里的a是必须要有双引号的!不然肯定是错的。
            counter += 1
    return counter
print("the number is: ")
print(how_many_a_in_this_string(my_name))

#示例2
def letter_check(word,letter):
    result = False
    for j in word:
        if letter == j:
            result = True
            break
    return result

##还有一个简单的写法，来完成上面的操作
# "x" in "ysasdax"  (如左边这种格式）

first = "a" in "haiyang"
second = "b" in "haiyang"
print(first)
print(second)

#例题
def contains(big_string, little_string):
    result = little_string in big_string
    return result
#还是例题，但是关系不大
def common_letters(string_one,string_two):
    result = []
    for i in string_one:
        for j in string_two:
            if i == j:
                result.append(j)
    result = list(dict.fromkeys(result))
    return result

print(commom_letters("apple","haiyang"))


# mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist)
#这些代码告诉我，如何去除一个list中的重复

#cheat sheet:
#https://www.codecademy.com/learn/paths/computer-science/tracks/cspath-python-objects/modules/cspath-python-strings/cheatsheet



