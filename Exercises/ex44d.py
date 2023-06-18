# 继承与组合

# 继承就是用来指明一个类的大部分或全部功能都是从一个父类中获得的。
# 父类和子类有 3 种交互方式：
# 1. 子类上的动作完全等同于父类上的动作（隐式继承）
# 2. 子类上的动作完全覆盖了父类上的动作（显示覆盖）
# 3. 子类上的动作部分替换了父类上的动作（在运行前或运行后替换）

# 隐式继承：
# 父类定义了一个函数，但没有在子类中定义时发生隐式继承。这时你还是可以从子类中调用子类没有，但父类有的函数。

# 显示覆盖：
# 当你需要让子类里的函数有不同的行为时，你需要覆盖子类中的函数。要做到这点，只需在子类中创建同名函数就行。
# 当你调用子类中同名函数时，执行的是子类中的同名函数，而不是父类中的同名函数。

# 在运行前或运行后替换：
# 当你进行了显示覆盖时，你想执行子类中的同名函数，然后再执行父类中的同名函数，或者反过来。
# 可以用「super(子类名，self).父类函数名()」来执行父类函数。
# 读作：用「子类名」和「self」这两个参数调用「super函数」，然后在此返回的基础上调用「父类函数」

# 定义一个父类 Parent
class Parent(object):

    # 父类函数 override
    def override(self):
        print("PARENT override()")

    # 父类函数 implicit, 在子类 Child 中隐式继承
    def implicit(self):
        print("PARENT implicit()")

    # 父类函数 altered
    def altered(self):
        print("PARENT altered()")

# 定义一个子类 Child，Child has-a Parent
class Child(Parent):

    # 子类函数 override，显示覆盖父类中的 override
    def override(self):
        print("CHILD override()")

    # 子类函数 altered，在运行前或运行后替换成父类中的 altered
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

# 实例化
dad = Parent()
son = Child()

# 隐式继承
dad.implicit()
son.implicit()

# 显示覆盖
dad.override()
son.override()

# 在运行前或运行后替换
dad.altered()
son.altered()