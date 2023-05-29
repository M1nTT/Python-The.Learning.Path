# ex23.2.py
# 找一些别的编码方式的字符串，放到 ex23.py 中，看看会出什么问题。

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

    # \U00006211\U00005728\U00005B66\U00000050\U00000079\U00000074\U00000068\U0000006F\U0000006E -- utf-32 --> 我在学Python
    print("\U00006211\U00005728\U00005B66\U00000050\U00000079\U00000074\U00000068\U0000006F\U0000006E", raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding, error)