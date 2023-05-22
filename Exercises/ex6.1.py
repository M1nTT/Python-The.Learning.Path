# ex6.1.py
# 通读这段程序，在每一行的上面写一条注释，给自己解释一下这一行的作用。

# 将 10 赋值给变量 tpyes_of_people
tpyes_of_people = 10
# 将带有格式化字符串的字符串赋值给变量 x
x = f"There are {tpyes_of_people} type of people."

# 将字符串赋值给变量
binary = "binary"
# 将字符串赋值给变量
do_not = "don't"
# 将带有格式化字符串的字符串赋值给变量 y
y = f"Those who know {binary} and those who {do_not}."

# 打印出变量 x & y
print(x)
print(y)

# 将变量 x & y 嵌入到格式化字符串中，打印出格式化字符串
print(f"I said: {x}")
print(f"I also said: '{y}'")

# 将字符串赋值给变量
hilarious = False
# 将带有 未指定的格式化字符串{} 的字符串赋值给变量 joke_evaluation
joke_evaluation = "Isn't that joke so funny? {}!"

# 指定变量 joke_evaluation 中未指定的格式化字符串为变量 hilarious,打印出变量 joke_evaluation
print(joke_evaluation.format(hilarious))

# 将字符串赋值给变量 w & e
w = "This is the left side of..."
e = "a String with a right side."

# 打印出变量 w 和 e
print(w + e)