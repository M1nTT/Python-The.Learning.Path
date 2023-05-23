# 提示和传递

# input() 函数中的提示词可以用一个变量来表示，前提是你先定义了这个变量是什么。这样的好处是修改变量一处即可同时更改多处的提示词。
# 多行格式化字符串的语法请看 Line: 22-26

from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
	Alright, so you said {likes} about liking me.
	You live in {lives}. Not sure where that is.
	And you have a {computer} computer. Nice.
	""")