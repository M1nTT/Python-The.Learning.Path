# ex21.2.py
# 这个脚本的结尾是一个谜题。我将一个函数的返回值用作了另一个函数的参数。我将它们链接到了一起，以便我能用函数创建一个公式。这样可能有些难度，不过运行一下你就知道结果了。接下来，你需要试试看能不能找出正常的公式来创建同样的一组运算。

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

what = subtract(add(24, divide(34, 100)), 1023)

print(f"24 + 34 / 100 - 1023 = {what}")