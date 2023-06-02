# ex33.1.py
# 将这个 while 循环改成一个函数，将测试条件(i < 6)中的6换成一个变量,并用不同的数进行测试。

# 函数需要用 return 返回结果
# argv 获取的是字符串形式，要对比数的大小只能是数和数比。使用int()将字符串转换成数的形式。

from sys import argv

script, top = argv

x = int(top)

i = 0
numbers = []


def While_Funtion(x):
    global i
    while i < x:
        numbers.append(i)
        i = i + 1

    return numbers

print(While_Funtion(x))