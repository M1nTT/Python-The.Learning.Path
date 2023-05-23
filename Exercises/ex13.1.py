# ex13.1.py
# 给你的脚本少于三个参数，看看会得到什么出错消息，试着解释一下。

# 得到如下消息：`python3.11 ex13.1.py 1 2`

"""
Traceback (most recent call last):
  File "/Users/macintosh/Documents/Python-The.Learning.Path/Exercises/ex13.py", line 19, in <module>
    script, first, second, third = argv
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: not enough values to unpack (expected 4, got 3)
"""

# 解释：
# argv 解包期望收到 4 个值，但是只收到了 3 个，所以解包失败。

from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second cariable is:", second)
print("Your third variable is:", third)