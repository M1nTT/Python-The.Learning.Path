# ex23.1.py
# 给每一行加注释

# 从sys软件包中导入 argv 并解包。
import sys
script, encoding, error = sys.argv


# 定义函数main： 需要三个参数
def main(language_file, encoding, errors):
    # 阅读 language_file 文件的一行，将阅读的内容赋值给line
    line = language_file.readline()
    # 如果 line 中发现了 \n，即继续执行下面缩进的代码，否则结束。
    if line:
        # 调用函数print_line, 输入三个参数 line、encoding、errors
        print_line(line, encoding, errors)
        # 再次调用 main 函数
        return main(language_file, encoding, errors)


# 定义函数print_line : 需要三个参数 line、encoding、errors，后两个从argv获取
def print_line(line, encoding, errors): 
    # 把line中每行结尾的 \n 删掉，删掉后的内容赋值给next_lang
    next_lang = line.strip() 
    # 对next_lang中的内容进行编码，使用argv获取的两个参数进行。
    raw_bytes = next_lang.encode(encoding, errors = errors)
    # 对raw_bytes 中的内容进行解码，使用argv获取的两个参数进行。
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    # 打印出字符串
    print(raw_bytes, "<===>", cooked_string)


# 打开 language.txt 文件
languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding, error)