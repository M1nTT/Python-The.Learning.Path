# 命名、变量、代码和函数

# def 函数的用法：
# 1. def 函数名():
# 2. 接下来一行四个空格，即一个缩进。
# 3. 使用 *args 则需要解包，或者直接在括号里放入变量,多个参数用逗号隔开，也可以什么都不放。
# 4. 调用函数时：函数名(参数)
# *args : 接受所有参数,然后放到args的列表中去。

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *argv is actually poinless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Zed","Snow")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()