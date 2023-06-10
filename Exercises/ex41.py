# 学习面向对象术语

# capitalize() 函数，将字符串的第一个字母变为大写，其余的所有变为小写
# str() 函数，将所有内容转换成字符串
# strip() 函数，删除所有空格
# count() 函数，输出指定字符出现的次数
# randint() 函数，返回指定范围内选定元素的整数，左右两边的数都包括
# key() 函数：输出字典里所有的key值
# list() 函数：将参数内容创建为字典
# shuffle() 函数：采用一个序列（例如随机序列），重新排列列表里的顺序

# 类（class）：告诉Python创建新类型的东西
# 对象（object）：两个意思，即最基本的东西，或某样东西的实例
# 实例（instance）：这是让python创建一个类时得到的东西
# def：这是在类里定义函数的方法
# self：在类的函数中，self指代被访问的对象或者实例的一个变量
# 继承（ingeritance）：指一个类可以继承另一个类的特性，和父子关系类似
# 组合（composition）：指一个类可以将别的类作为它的部件构建起来，有点像车子和轮子的属性
# 属性（attribute）：类的一个属性，它来自于组合，而且通常是一个变量。
# 是什么（is-a）：用来描述继承关系，如Salmon is-a Fish（鲑鱼是一种鱼）
# 有什么（has-a）：用来描述某个东西是由另外一些东西组成的，或者某个东西有某个特征，如Salmon has-a mouth（鲑鱼有一张嘴）

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

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

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

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
        
    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)
    
    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")