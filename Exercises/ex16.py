# 读写文件

# close     	 -> 关闭文件
# read      	 -> 读取文件内容
# readline  	 -> 只读取文本文件中的一行
# truncate  	 -> 清空文件，请小心使用该命令
# write('stuff') -> 将「stuff」写入文件
# seek(0) 		 -> 将读写位置移动到文件开头

# open() 函数的参数介绍：target = open(filename, 'w')
# w: 写入 r: 读取 a: 追加
# 若无参数，即：open(filename), 则默认使用「 r 」只读模式
#
# 模式  ｜ 可做操作  ｜ 若文件不存在  ｜  是否覆盖
# r     -> 只读 		 	报错 			否
# r+	-> 可读写		报错 			是
# w 	-> 只写 			创建 			是
# w+	-> 可读写  		创建 			是
# a 	-> 只写 			创建 			否，追加写
# a+ 	-> 可读写 		创建 			否，追加写

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (CTRL-Z).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three line.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we clost it.")
target.close()