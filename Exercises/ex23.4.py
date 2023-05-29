# ex23.4.py
# 在Python解码系统不出错的前提下，你能破坏到什么程度？


def main(language_file):
    line = language_file.readline()
    if line:
        raw_bytes = line.encode()
        print(raw_bytes, "<===>", line)

        return main(language_file)


main(open("languages.txt"))