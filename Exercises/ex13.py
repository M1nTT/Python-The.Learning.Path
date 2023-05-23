# 参数、解包和变量

# 脚本(script)： .py 程序
# 参数(argument)： 在命令行键入 `python3.11 ex1.py` ex1.py 就是参数。
# import 语句：这是将 Python 的「特性」引入脚本的方法，Python 不会一下子将所有的特性给你，而是让你需要什么就取什么。「特性」也即「模块」(moudule)
# argv 即所谓的参数变量(argument variable)，这个变量保存着你运行 Python 脚本时传递给 Python 脚本的参数。
# 解包(unpack)：Line 11，把 argv 中的东西取出，解包，将所有的参数依次赋值给左边的这些变量。

# 运行逻辑：
# 1. 脚本从 sys 库中调用了 argv 模块
# 2. 程序开始时，你需要自行输入 argv 模块中的 3 个命令行参数（也即：字符串）。
# 3. 程序收到你输入的 3 个变量，并分别赋值给 first second third。
# 4. 程序打印出指定字符串，字符串中包含了变量的值。

# *启用此脚本* `python3.11 ex13.py first 2nd 3rd` 你可以将 first 2nd 3rd 替换成任意值。

from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second cariable is:", second)
print("Your third variable is:", third)