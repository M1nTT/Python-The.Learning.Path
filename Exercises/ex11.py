# 提问

# end=' ' -> 告诉 Python 不要用换行符结束这一行跑到下一行去。
# 函数 input() 为输入函数，让代码执行者输入一个字符串，并将这个字符串赋给左边的变量。
# 函数 int() 可将数值转换为整数。
# x = int(input()), 它会从 input() 获取字符串形式的数值，然后用 int() 把它转换成整数。

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")