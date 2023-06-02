# while 循环

# while 循环：只要循环语句中的布尔值为 True，while 循环就会不停地执行它下面的代码块
# 注意事项：
# 1. 尽量少用 while 循环，大部分时候 for 循环是更好的选择
# 2. 重复检查你的 while 语句，确定你测试的布尔表达式最终会变成 False
# 3. 如果不确定，就在 while 循环的开始和结尾打印出你要测试的值，看看它的变化

# i 要定义全局才能在函数里使用
# 函数需要用 return 返回结果
# argv 获取的是字符串形式，要对比数的大小只能是数和数比较。使用int()将字符串转换成数的形式。


i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now:", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)