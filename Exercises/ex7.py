# 更多打印

# .format() 函数中可以直接使用字符串，而不一定要是变量。若是字符串需要带上引号（''), 若是变量则不用。
# "." * 10  -> ..........
# end=' ' -> 输出一个空格，并且不换行继续执行后面的代码
# 创建字符串的时候单引号和双引号都可以，但是一般单引号用来创建简短的字符串。若是字符串中需要使用引号，外层用单引号，内容用双引号会更加好看。

print("Mary had a little lame.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that mary went.")
print("." * 10) # What'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)