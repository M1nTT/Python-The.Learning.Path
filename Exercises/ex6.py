# 字符串和文本

# 格式化字符串可以直接赋值给变量 Line: 8、12
# 变量里的变量可以为空 Line: 21 ;再在打印项中利用 .format() 函数指定{}中的变量 Line: 23
# 变量 x 可以直接打印出 Line: 28

tpyes_of_people = 10
x = f"There are {tpyes_of_people} type of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny? {}!"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a String with a right side."

print(w + e)