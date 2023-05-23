# ex13.2.py
# 将 input 和 argv 一起使用，让脚本从用户那里得到更多的输入。不要想多了，只是用 argv 的到一些东西，用 input 从用户那里得到另一些东西。

# argv 和 input 有何不同？
# 不同点在于用户输入的时机。如果是参数是在用户执行命令的时候就要输入，那就用 argv，如果是在脚本运行过程中需要用户输入，那就用 input()。

from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv
x = input("This is input, enter anything！ ")

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second cariable is:", second)
print("Your third variable is:", third)

print("This is what you typed:", x)