# 函数和文件

# readline() 函数是怎么知道每一行在哪？
# readline() 里面的代码会扫描文件的每一个字节，直到找到一个 \n 为止，然后它停止读取文件，并且返回此前发现的文件内容。文件 f 会记录每次调用 readline() 后读取的位置，这样它就可以在下次调用时读取接下来的一行了。

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three line:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)