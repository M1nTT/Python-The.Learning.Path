# ex16.1.py
# 写一段与上一个习题类似的脚本，使用 read 和 argv 读取你刚才新建的文件。

from sys import argv

script, filename = argv

txt1 = open(filename)

print(f"Here's your file {filename}")
print(txt1.read())

txt1.close()

print("Let's enter the file name again：")
filename2 = input("> ")
txt2 = open(filename2)

print(txt2.read())

txt2.close()