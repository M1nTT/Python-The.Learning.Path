# 更多更多的练习

# split() 函数：通过指定分隔符对字符串进行切片，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# pop() 函数：移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。0：第一个 1：第二个 2：第三个 -1：最后一个
# sorted() 函数：默认对序列中元素进行升序排序，会生成新列表，不改变原列表。
# def 函数中，使用 """文档注释""" 定义文档注释(documentation comment)
# 调用文档注释： 终端：python3.11  // import ex25 // help(ex25) or help(ex25.break_words) 


def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping if off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence
    print_first_word(words)
    print_last_word(words)