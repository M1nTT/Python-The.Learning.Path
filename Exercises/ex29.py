# if 语句

# if 的判断条件（布尔表达式）为真，则执行下面缩进的代码，否则跳过执行。
# 只要一行以冒号结尾，下面的内容就要有缩进。

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("people are dogs.")
