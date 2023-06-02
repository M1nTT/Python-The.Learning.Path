# ex33.2.py
# 用函数添加另一个参数，这个参数用来定义第 21 行的 +1，这样你就可以任意递增了。 line21:    i = i + 1

from sys import argv

script, top, increase, start = argv

x = int(top)
y = int(increase)
i = int(start)

numbers = []


def While_Funtion(x, y, i):
    while i < x:
        numbers.append(i)
        i = i + y

    return numbers

print(While_Funtion(x, y, i))