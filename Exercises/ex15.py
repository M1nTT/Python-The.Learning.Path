# 读取文件

# 要用脚本打开其他文件，不应该把要被打开的文件的文件名写死在此脚本中，最好用 argv 或 input 让用户自己输入要打开的文件的文件名。
# open() 函数：接收一个参数，并且返回一个值，你可将这个值赋给一个变量。这是打开文件的过程。
# read() 函数：txt.read() -> 嘿 txt！执行 read 命令，无需任何参数。
# close() 函数：用来关闭打开的文件，文件名.close()。例子在 ex15.4.py
# sys 是一个软件包，里面有 argv 模块。

# filename 名称为：ex15_sample.txt

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())