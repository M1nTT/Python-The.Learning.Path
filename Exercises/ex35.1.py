# ex35.1.py
# 为你不懂的函数写注释



from sys import exit

# 关卡1 - gold_room
def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    # 纯数字，有 1 或 0 ，将内容转成整数赋值给 how_much
    # 纯数字，没有 0 或 1 ，**游戏结束**
    # 非纯数字，python 会报错：invalid literal for int() with base 10: 'ttt20'
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    # 如果 how_much 变量里的数值小于50，**胜利**
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    # 如果 how_much 变量里的数值大于等于50，**游戏结束**
    else:
        dead("You greedy bastard!")


# 关卡2 - bear_room
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    # bear_moved 的初始值设定为 False
    bear_moved = False

    # 无限循环执行下列代码
    while True:
        choice = input("> ")

        # 如果 choice 的内容中含有 take honey，**游戏结束**
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        # 如果 choice 的内容中含有 taunt bear，且 bear_moved = Flase ,则执行缩进代码：打印语句，将 bear_moved 的值转为 True
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        # 如果 choice 的内容中含有 taunt bear，且 bear_moved = True，**游戏结束**
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        # 如果 choice 的内容中含有 open door，且 bear_moved = True，**进入关卡1**
        elif choice == "open door" and bear_moved:
            gold_room()
        # 打印提示内容，然后重新循环 while 函数，直到上面跳转出此 While 函数为止
        else:
            print("I got no idea what that means.")


# 关卡3 - cthulhu_room
def cthulhu_room():
    print("Here you see the great evil Cthulhu")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input ("> ")

    # 如果 flee 在内容中，**游戏重新开始**
    if "flee" in choice:
        start()
    # 如果 head 在内容中，**游戏结束**
    elif "head" in choice:
        dead("well that was tasty!")
    # **重新开始关卡3**
    else:
        cthulhu_room()


# 死亡
def dead(why):
    print(why, "Good job!")
    exit(0)

# 游戏开始
def start():
    print("You are in adark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")
    
    # 如果用户输入内容为 left，**进入关卡2**
    if choice == "left":
        bear_room()
    # 如果用户输入内容为 right，**进入关卡3**
    elif choice == "right":
        cthulhu_room()
    # 否则，**游戏结束**
    else:
        dead("You stumble around the room until you starve.")


start()

