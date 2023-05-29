# 字符串、字节串和字符编码

# 字符串：string 字节串：bytes
# bit(位): 只有1和0。 1 -> 开 // 0 -> 关
# byte(字节): 1 byte = 8 bit ；一字节可以编写一个英文字符，如：Z ; 1byte 可以表示256个数字
# ASCII(美国信息交换标准代码): 把数字和字母相互对应。 1011010 -> 90 -> z ; 二进制(一字节) -> 数字 -> 字母
# Unicode：所有人类语言的通用编码(universal encoding), 32位，可以存储4,294,967,295（2^32）个字符，足以存在所有人类语言，多余的存储表情。
# 32位（32/8=4）是4字节，对于要编码的大部分类型的文本是种浪费。所以我们把大部分常用字符用8位编码，需要的时候再用16位或者32位。这种约定在python里叫UTF-8(Unicode Transformation format 8 Bits)。
# b'.....' 告诉python ......为原始字节串

# bytes -- .decode()解码 --> string ；bytes 不包含编码方式，你要告诉python用什么方式解码（UTF-8）
# string -- .encode()编码 --> bytes 
# 记忆：解码字符串，编码字节串，DBES

# strip() 函数: 用于去除字符串开头和结尾的空白字符（包括空格、制表符、换行符等等）的一个函数。如果没有传递参数，则默认去除空白字符。
# encode() 函数: 给字符串编码，需要两个参数（编码方式，处理错误的方式）
# decode() 函数: 给字节串解码，需要两个参数（编码方式，处理错误的方式）

import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors): 
    next_lang = line.strip() 
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding, error)