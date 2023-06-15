# ex42.1.py
# 在这个习题中为 animals、fish 和 people 添加一些函数，让它们做一些事情。
# 看看当函数在 Animal 这样的“基类”（base class）里和在 Dog 里会发生什么一样的事情。

# 答：基类不需要参数，其他类需要参数

class Animal(object):
    
    def x(name):
        name = str(name)
        name += "HAHA"
        print(name)
    pass



class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name
    
    def x(name):
        name = str(name)
        name += "HAHA"
        print(name)


Oh1 = Animal.x("Doggggg")
aH1 = Dog.x("Doggggg")
Oh1 = Animal.x(111)
aH1 = Dog.x(111)

AAA = Animal()
BBB = Dog()

#macintosh@192 Exercises % python3 ex42.1.py
#DogggggHAHA
#DogggggHAHA
#111HAHA
#111HAHA
#Traceback (most recent call last):
#  File "/Users/macintosh/Documents/git-repos/Python-The.Learning.Path/Exercises/ex42.1.py", line 32, in <module>
#    BBB = Dog()
#          ^^^^^
#TypeError: Dog.__init__() missing 1 required positional argument: 'name'