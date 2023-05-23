# ex15.1.py
# 为每一行加上注释，说明这一行的用途。

# 从 sys 中导入 argv 模块
from sys import argv

# 解包 argv 模块
script, filename = argv

# 使用 open() 函数接受参数：filename，并且返回一个值，将这个值赋给 txt 变量
txt = open(filename)

# 打印格式化字符串
print(f"Here's your file {filename}:")
# 使用 read() 函数打印变量 txt 的值
print(txt.read())

# 打印字符串
print("Type the filename again:")
# 使用 input() 函数，并用提示词让用户输入字符串，并将字符串赋值给 file_again 变量
file_again = input("> ")

# 使用 open() 函数接受参数：file_again，并且返回一个值，将这个值赋给 txt_again 变量
txt_again = open(file_again)

# 使用 read() 函数打印变量 txt_again 的值
print(txt_again.read())