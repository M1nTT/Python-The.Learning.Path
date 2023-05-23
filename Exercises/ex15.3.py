# ex15.3.py
# 只用 input 写这个脚本，想想那种获取文件名称的方法更好，为什么。

# 答：
# 如果脚本可以做到从开始到结束，全部执行完都不需要输入任何命令的情况下就能完成功能，用 argv 会更好。因为这样代码可以无人值守运行。
# 但如果你的脚本的功能运行中，涉及多次输入，并且调用的文件名经常变更，或者这个脚本只是完成一个功能的话，用 input 会更好。
# 如果用 input 可以加入提示词，让用户知道该输入什么，而 argv 不行。
# input 用的代码会少很多。
# 总之要具体情况具体分析，看你追求什么。

# filename 名称为：ex15_sample.txt

print("Type the filename:")
filename = input("> ")

txt = open(filename)

print(txt.read())