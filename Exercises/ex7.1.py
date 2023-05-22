# ex7.1.py
# 倒着阅读这段代码，在每一行的上面加一条注释

# 打印字符串
print("Mary had a little lame.")
# 将 snow 赋值给未指定的格式化字符串，并打印出结果
print("Its fleece was white as {}.".format('snow'))
# 打印字符串
print("And everywhere that mary went.")
# 将 "." 的数量乘 10，打印出来
print("." * 10) # What'd that do?

# 将字符串赋值给变量
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
# 打印出 end1 和 end2 ... end6, 在打印一个空格，并且不换行接着执行下面的代码
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# 打印出 end7 和 end8 ... end12
print(end7 + end8 + end9 + end10 + end11 + end12)