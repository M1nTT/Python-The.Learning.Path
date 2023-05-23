# ex14.1.py
# 给你的脚本再添加一个参数，并使用这个参数，格式和前一个习题中的 first, second = ARGV 一样。

from sys import argv

script, user_name, gender = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print(f"I know your gender is {gender}, this is great.")
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