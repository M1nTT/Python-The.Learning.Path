# 继承与组合

# 多重继承：是指你定义的类继承了一个或多个类，就像：class SuperFun(Child, BadStuff)
# 这表示你创建了一个类 SuperFun，它同时继承了 Child 和 BadStuff 两个类。
# 一旦你在 SuperFun 上调用任何隐式动作，Python就必须回到 Child 和 BadStuff 的类层结构中查找可能的函数，而且必须用固定的顺序查找。
# 为了实现这点，Python 用了一个叫「方法解析顺序（method resolution order，MRO）的东西和一个叫 C3 的算法。

# 组合
# 继承是一种很有用的技术，不过还有一种实现相同功能的方法，就是直接使用别的类和模块，而非依赖于隐式继承。

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()