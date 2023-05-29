# ex23.3.py
# 额外挑战：使用b''字节串取代UTF-8字符串重写代码，结果就是把程序反写一遍。

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

    print(raw_bytes)


languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding, error)