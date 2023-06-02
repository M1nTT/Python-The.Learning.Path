# ex33.3.py
# 使用 for 循环和 range 把这个脚本再写一遍。还需要中间的递增操作吗？如果不去掉它，会有什么样的结果。

# 答1: 不需要中间的递增操作了。
# 答2: 如果不去掉，不影响numbers的结果，但会影响i的结果


i = 0
numbers = []

for i in range(0, 6):
    numbers.append(i)
    i = i + 1

print(numbers)
print(i)