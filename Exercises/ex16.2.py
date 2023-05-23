# ex16.2.py
# 这个文件重复的地方太多了。试着用一个 target.write() 将 line1、line2 和 line3 打印出来，替换掉原来的 6 行代码。你可以使用字符串、格式化字符和转译字符。

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (CTRL-Z).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three line.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3)

print("And finally, we clost it.")
target.close()