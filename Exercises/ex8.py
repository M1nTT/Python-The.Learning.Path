# 打印，打印

# 对于变量中有多个「未指定格式化字符串」的情况，若要使用 .format() 函数进行指定，有几种情况。
# 1. 若对每个含「未指定格式化字符串」的变量进行指定，且指定的是「数字」的话，则每个指定中用 "," 分开，并且数字不用加引号。
# 2. 若对每个含「未指定格式化字符串」的变量进行指定，且指定的是「字符串」的话，则每个指定同样用 "," 分开，并且每个字符串需要用引号括起来。若字符串过长，可以分行缩进排列。
# 3. 若对每个含「未指定格式化字符串」的变量进行指定，且指定的是「Ture / False 这类的关键字」的话，则和指定数字的要求一样。
# 4. 若对每个含「未指定格式化字符串」的变量进行指定，且指定的是「变量」的话，则和指定数字的要求一样。



formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
))