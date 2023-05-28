# ex20.1.py
# 为每一行加上注释，以便理解这一行的作用。

# 从 sys 中调用 argv
from sys import argv

# 解包 argv
script, input_file = argv

# 定义函数 print_all: 接受一个参数，然后用read()函数打开它
def print_all(f):
    print(f.read())

# 定义函数 rewind: 受一个参数，然后将磁头移到这个文件的开头
def rewind(f):
    f.seek(0)

# 定义函数 print_a_line: 接受两个参数，一个是行数，一个是文件名，然后打印行数，在打印文件指定的行数的内容。
def print_a_line(line_count, f):
    print(line_count, f.readline())

# 将用户输入的文件 input_file 打开到 current_file
current_file = open(input_file)

# 打印字符串
print("First let's print the whole file:\n")

# 调用 print_all 函数，参数是 curren_file
print_all(current_file)

# 打印字符串
print("Now let's rewind, kind of like a tape.")

# 调用 rewind 函数，参数是 current_file
rewind(current_file)

# 打印字符串
print("Let's print three line:")

# 定义变量 current_line 的值为1
current_line = 1
# 调用函数 print_a_line，参数是 current_line 和 current_file
print_a_line(current_line, current_file)

# 变量 current_line 的最新值为原值加一
current_line = current_line + 1
# 调用函数 print_a_line，参数是 current_line 和 current_file
print_a_line(current_line, current_file)

# 变量 current_line 的最新值为原值加一
current_line = current_line + 1
# 调用函数 print_a_line，参数是 current_line 和 current_file
print_a_line(current_line, current_file)