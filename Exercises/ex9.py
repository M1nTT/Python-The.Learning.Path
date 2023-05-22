# 打印，打印，打印

# \n 为换行符(new line character)，其后的代码都将在下一行执行。
# 对于超长字符串，可以使用 (""")和(""") 将字符串整体括起来，然后字符串内部可以用键盘按键 (Enter - 回车) 来分行。

# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 line if we want, or 5, or 6.
""")