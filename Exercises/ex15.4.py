# ex15.4.py
# 让你的脚本针对 txt 和 txt_again 变量也调用下 close()。处理完文件后需要将其关闭，这是很重要的一点。

# close() 函数：用来关闭打开的文件，文件名.close()

# filename 名称为：ex15_sample.txt

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()