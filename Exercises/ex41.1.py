# ex41.1.py
# 注释你不懂得代码

# 代码运行解释：
# 1.导入了一些必要的模块和库，包括random、urlopen和sys。
# 2.定义了一些常量，如WORD_URL和PHRASES。
# 3.根据命令行参数确定是否首先练习短语（PHRASE_FIRST）。
# 4.从指定的网址加载单词列表并保存在WORDS中。
# 5.定义了一个名为convert的函数，用于将给定的snippet(key)和phrase(value)转换为问题(question)和答案(answer)。
# 6.在一个无限循环中，从PHRASES中随机选择一个key，调用convert函数生成相应的问题(question)和答案(answer)，并将其展示给用户。
# 7.用户输入答案后，显示正确答案。
# 8.当用户按下CTRL-Z时，循环结束，程序退出。

import random
from urllib.request import urlopen
import sys

# 从网页获取单词
WORD_URL = "http://learncodethehardway.org/words.txt"
# 存放所有下载单词的列表
WORDS = []

# key and value 作为问题和答案
PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
      "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}


# 若用户额外输入一个参数，且参数是english，则PHRASE_FIRST为True，否则为False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# 从网站上加载单词，删除空格后，以utf-8的格式转换成字符串，然后放到WORDS列表里
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))


# convert函数：
# 将 snippet(key) 里的%%%/***/@@@替换为WORDS列表里随机选择后的单词
# 将 phrase(value) 里的%%%/***/@@@替换为WORDS列表里随机选择后的单词
# 返回snippet和phrase替换后的句子，作为questiion和answer
def convert(snippet, phrase):
    # snippet(key) 中有几个「%%%」，就从WORDS中随机选几个单词，并将其首字母大写，其余全小写
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    # snippet(key) 中有几个「***」，就从WORDS中随机选几个单词
    other_names = random.sample(WORDS, snippet.count("***"))
    # 储存最终结果
    results = []
    # 在 snippet(key) 中有「@@@」的情况下，在WORDS中随机选1-3个单词，并将单词用逗号隔开（也就是说参数可以有1-3个）
    param_names = []

    # 若key中有@@@则执行循环，否则跳过
    for i in range(0, snippet.count("@@@")):
        # 在WORDS中随机选取1-3个单词，用逗号分隔开后添加到param_names里
        param_count = random.randint(1, 3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))
    
    # 将snippet(key)和phrase(value)里%%%/***/@@@分别替换成class_names/other_names/param_names里的单词
    for sentence in snippet, phrase:
        # result = snippet(key):phrase(value)
        result = sentence[:]

        # 将result里的「%%%」替换成class_names里的单词
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # 将result里的「***」替换成other_names里的单词
        for word in other_names:
            result = result.replace("***", word, 1)

        # 将result里的「***」替换成param_names里的单词
        for word in param_names:
            result = result.replace("@@@", word, 1)

        # 将替换后的内容保存至results
        results.append(result)
    
    # 返回results
    return results


# try：测试代码是否发生错误，是的话执行except的内容
try:
    while True:
        # 将PHRASES里所有的key值创建成字典，赋值给snippet
        snippets = list(PHRASES.keys())
        # 随机排列snippet(key)里的内容(Key)的顺序
        random.shuffle(snippets)

        for snippet in snippets:
            # 获取字典key里对应的value
            phrase = PHRASES[snippet]
            # 将snippet(key)和phrase(value)转换成question和answer
            question, answer = convert(snippet, phrase)
            # 如果PHRASE_FIRST为True，则将answer和question对调
            if PHRASE_FIRST:
                question, answer = answer, question

            # 打印出问题
            print(question)

            # 用户输入提示
            input("> ")
            # 不论用户输入什么，打印出答案
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")