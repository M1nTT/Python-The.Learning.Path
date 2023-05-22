# ex6.2.py
# 找出所有“把一个字符串放进另一个字符串”的位置。总共四处。


tpyes_of_people = 10
# 第一处
x = f"There are {tpyes_of_people} type of people."

binary = "binary"
do_not = "don't"
# 第二处
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# 第三处
print(f"I said: {x}")
# 第四处
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny? {}!"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a String with a right side."

print(w + e)