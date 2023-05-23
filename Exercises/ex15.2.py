# ex15.2.py
# 删掉 10～15 行用到 input 的部分，再运行一遍脚本。

# filename 名称为：ex15_sample.txt


from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())