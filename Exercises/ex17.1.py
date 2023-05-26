# ex17.1.py
# 看看你能把脚本改多短，我可以把它变成一行

from sys import argv

script, from_file, to_file = argv

indata = open(from_file).read()
open(to_file, 'w').write(indata)