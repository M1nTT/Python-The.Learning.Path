# 那是什么

# 转译序列(escape sequence)

### 单双引号转译 
# 1. “I am 6'2\" tall." # 将字符串中的「单引号」转译：'2\"
# 2. “I am 6\'2" tall." # 将字符串中的「双引号」转译：\'2"
# 3. 或者不转译，直接使用 (""") 将内容括起来。

### 转译符号
# \\ -> 反斜杠(\)
# \' -> 单引号(')
# \" -> 双引号(")
# \a -> ASCII 响铃符(BEL)
# \b -> ASCII 退格符(BS)
# \f -> ASCII 进纸符(FF)
# \n -> ASCII 换行符(LF)
# \r -> ASCII 回车符(CR)
# \t -> ASCII 水平制表符(TAB)
# \v -> ASCII 垂直制表符(VT)
# \ooo -> 值为八进制值 ooo 的字符
# \xhh -> 值为十六进制值 hh 的字符
# \uxxxx -> 值为 16 位十六进制 xxxx 的字符
# \Uxxxxxxxx -> 值为 32 位十六进制值 xxxxxxxx 的字符
# \N{name} -> Unicode 数据库中的字符名，其中 name 是它的名字，仅 Unicode 适用。


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)