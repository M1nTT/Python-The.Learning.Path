# ex21.1.py
# 如果你不是很确定 return 的功能，试着自己写几个函数，让它们返回一些值。你可以将任何可以放在 = 右边的东西作为一个函数的返回值。

def add_multiply(a, b, c, d):
    print(f"y = ({a} * {b}) + ({c} * {d})")
    return a * b + c * d

result = add_multiply(1, 2, 1, 3)

print(f"y = {result}")