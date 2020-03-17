#概括：这个章节主要就是 介绍，多种用于string的method
# 这一节中一共学习了这些东西:
# .upper(), .title(), and .lower() adjust the casing of your string.
# .split() takes a string and creates a list of substrings.
# .join() takes a list of strings and creates a string.
# .strip() cleans off whitespace, or other noise from the beginning and end of a string.
# .replace() replaces all instances of a character/string in a string with another character/string.
# .find() searches a string for a character/string and returns the index value that character/string is found at.
# .format() and f-strings allow you to interpolate a string with variables.

#1.这不是一个string method, string method的格式都如这样: 'Hello world'.upper() , 就像这样在末尾的，才能算一个string method
s1 = "Haiyang Jiang"
the_length_of_s1 = len(s1)
print(the_length_of_s1)

#2. Formatting Methods 改变string格式的几种方法，把全部变小写，全部变大写，把这个string里的所有第一个字母变大写
s2 = " haiyanG JIAng is a good BOy"
print("第二个，格式的演示")

print(s2.lower())
print(s2.upper())
print(s2.title())#标题格式，一句话里所有单词的第一个字母都变成了大写。

#3.Splitting Strings, 把strings分割成好多个部分，每个部分都变成一个元素，然后这些元素被储存在列表之中。
# .split() is performed on a string, takes one argument, and returns a list of substrings found between the given argument.
# delimiter 就是定界符的意思
# .split() 如果这个括号里啥都没有写，那系统默认用空格把这些语句给分隔开。
line_one = "The sky has given over"
line_one_words= line_one.split()
print(line_one_words)

## provide an argument for .split()
###be careful! this argument should be provided as a string itself, 就是这个参数，必须是，string里的一部分。
test_string = "hai_yang_jiang"
out_put = test_string.split("_") #其实，我们在前面学过，string是完全无法修改的，所以其实用了split，string是没有任何变化的，
#必须得新建一个变量，来储存这个被我们切割后的string
print(out_put)

#use escape sequences转义序列，
# \n 反斜杠 + n 表示 新的一行
# \t 表示的是 Horizontal tab，似乎就是自动往右边移四格。
print("hi \nmy friend!") #这里就是换行了
print("\thi my friend")#这里就是自动空了四格

test_strings =\
"""Hi
my friend
how are you?
are you happy?"""

#注意我在这里加了一个反斜杠,其实不加也是可以的，只要你紧跟着=号之后写就可以了。
test_out_put = test_strings.split('\n') #这是我发现的\n的另外一种用法，上面的string里面并不能找到这个，但是
#换行了！ 可能换行就算一种 \n把
print(test_out_put)

#4.Joining strings 前面的是把一个string拆分成好多个elements并储存在一个list里，而这个method就是把分开的elements给重新加起来。
#格式是这样的: 'delimiter'.join(list_you_want_to_join)
#在.join左边的是以后连成一长串后，这些elements之间间隔的东西。而在括号里就是那个list，这个list里面有很多元素，等下要被连接在一起。

link_these_words_together = ["I","want","to","link","these","words","together"]
new_string = " ".join(link_these_words_together)
print(new_string)

#还可以把 \n这样的转义符 当作 delimiter
poem_lines = ["hello","my baby","how are you?","have a nice day","god, I hate coding"]
poem = '\n'.join(poem_lines)
print(poem)#打出来的效果就是，打印一句，换行，再打印一句。

#5.去除多余的空格(或一切）
#.strip() 去除左右两边所有的空格
#.strip('!') 去除左右两边所有的感叹号

test5 = "    haiyang jiang    "
result5 = test5.strip()
print(result5)

test5_1 = "!!!!!haiyang jiang!!!!"
result5_1 = test5_1.strip("!")
print(result5_1)

#6.replace
#格式是这样的：string_name.replace(character_being_replaced, new_character)
test6 = "haiyan"
test7 = test6.replace("haiyan","haiyang")
print(test7)

#7.查找一个string里面特定的数据，将返回一个index
#首先，可以用来找字母
test7 = 'haiyang jiang'
output7 = test7.find('a')
print(output7)#原来只会显示这个string里面的第一个a

#其实可以用来 找一个词
god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)
#最后输出的答案是20，这个20，是这个单词，开头第一个字母所在的index，刚开始不接受，仔细一想，挺科学！

#8.including a variable in a string
#注意：这个与上面的是不一样的，这是一个method，你需要调用这个method，并且在里面添加一些数据。
#格式如下：
# def favorite_song_statement(song, artist):
#    return "My favorite song is {} by {}.".format(song, artist)

def say_two_worlds_to_you(word1,word2):
    result = "hi, friende. you are a {} and {}.".format(word1,word2)
    print (result)

say_two_worlds_to_you("bitch","cyka")

#上面的这种形式，虽然简便，但是如果括号特别多的话，就会出现混淆，所以下面这种方式出来了。
def favorite_song_statement(input1, input2):
    return "My favorite song is {song} by {artist}.".format(song=input1, artist=input2)
print(favorite_song_statement("xiaomotuo","unknown"))
