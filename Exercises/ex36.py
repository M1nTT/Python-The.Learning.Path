# 设计和调试

# 你应该选择 Macbook pro 14寸还是16寸？

from sys import exit

# 记分处
M_14 = 0
M_16 = 0

prompt = "\n输入纯数字 > "

### 第一部分：开头

def start():
    print("""
    你决定买一台 Macbook_Pro,
    但你不知道选择14寸还是16寸.
    我将问你一系列问题,
    从而给你答案。
    """)

    print("是否开始？")
    print("1. 开始")
    print("2. 退出")
    go_on = input(prompt)

    if go_on == "1":
        Q_01()
    elif go_on == "2":
        Goodbye("好的，程序已经退出……")
    else:
        Pure()
        start()



### 第二部分：程序功能

# 退出
def Goodbye(why):
    print("\n", why)
    exit(0)

# 输入提示
def Pure():
    print("**********输入错误：请输入纯数字**********")


# 输出结果
import random

def done():
    if M_14 > M_16:
        print("-------------------")
        print("问答结束:14寸更适合你")
        print("-------------------")
        exit(0)
    elif M_14 == M_16:
        M_14 + random.randint(-2,2)
        if M_14 > M_16:
            print("-------------------")
            print("问答结束: 14寸更适合你")
            print("-------------------")
            exit(0)
        else:
            print("-------------------")
            print("问答结束: 16寸更适合你")
            print("-------------------")
            exit(0)
    else:
        print("-------------------")
        print("问答结束: 16寸更适合你")
        print("-------------------")
        exit(0)



### 第三部分：问题

# Q_01 你的性别？
def Q_01():
    print("\n")
    print("& 你的性别？")
    print("1. 男\n2. 女\n3. 其他")

    x = input(prompt)
    global M_14; global M_16
    
    # 记分环节
    if x == "1":
        M_16 += 1
        Q_02()      #
    elif x == "2":
        M_14 += 1
        Q_02()
    elif x == "3":
        M_14 += 1
        M_16 += 1
        Q_02()
    else:
        Pure()
        Q_01()


# Q_02 你的性别？
def Q_02():
    print("\n")
    print("& 预算是？")
    print("1. 15000-20000 CNY\n2. 20000-25000 CNY\n3. 25000- CNY")

    x = input(prompt)
    global M_14; global M_16
    
    # 记分环节
    if x == "1":
        M_14 += 1
        Q_03()      #
    elif x == "2":
        M_14 += 1
        M_16 += 1
        Q_03()
    elif x == "3":
        M_16 += 1
        Q_03()
    else:
        Pure()
        Q_03()


# Q_03 16寸对你来说是否有压迫感
def Q_03():
    print("\n")
    print("& 16寸对你来说是否有压迫感?")
    print("1. 是\n2. 否")

    x = input(prompt)
    global M_14; global M_16
    
    # 记分环节
    if x == "1":
        M_14 += 1
        Q_04()      #
    elif x == "2":
        M_16 += 1
        Q_04()
    else:
        Pure()
        Q_03()

# Q_04 是否会外接屏幕？
def Q_04():
    print("\n")
    print("& 是否会外接屏幕?")
    print("1. 是\n2. 否")

    x = input(prompt)
    global M_14; global M_16
    
    # 记分环节
    if x == "1":
        M_14 += 1
        Q_05()
    elif x == "2":
        M_16 += 1
        Q_05()
    else:
        Pure()
        Q_04()

# Q_05 平均一周外带几次？
def Q_05():
    print("\n")
    print("& 平均一周外带几次?")
    print("1. 0次\n2. 1-3次\n3. 4-7次\n4. 7次以上")

    x = input(prompt)
    global M_14; global M_16
    
    # 记分环节
    if x == "1":
        M_14 += 1
        M_16 += 1
        Q_06()
    elif x == "2":
        M_16 += 1
        Q_06()
    elif x == "3":
        M_14 += 1
        Q_06()
    elif x == "4":
        M_14 += 2
        Q_06()
    else:
        Pure()
        Q_05()


# Q_06 便携性
def Q_06():

    print("\n")
    print("& 通勤方式？")
    print("1. 走路\n2. 公共交通\n3. 自行车\n4. 汽车")
    
    y1 = int(input(prompt))

    print("\n")
    print("& 你的背包？")
    print("1. 勉强装下14寸\n2. 轻松装下14寸\n3. 轻松装下16寸")

    y2 = int(input(prompt))

    print("\n")
    print("& 通勤时间？")
    print("1. 30分钟以上\n2. 30分钟以下\n3. 无需通勤")
    
    y3 = int(input(prompt))

    global M_14; global M_16
    Y = y1 + y2 + y3

    if Y < 3:
        M_14 += 2
        Q_07()
    elif 3 <= Y <= 6:
        M_14 += 1
        M_16 += 1
        Q_07()
    else:
        M_16 += 2
        Q_07()


# Q_07 性能
def Q_07():

    numbers = []

    print("\n")
    print("& 是否经常使用多窗口？")
    print("1. 是\n2. 否")
        
    h1 = int(input(prompt))
    numbers.append(h1)

    print("\n")
    print("& 是否依赖状态栏？")
    print("1. 是\n2. 否")
        
    h2 = int(input(prompt))
    numbers.append(h2)

    print("\n")
    print("& 是否需要高负载？")
    print("1. 是\n2. 否")
        
    h3 = int(input(prompt))
    numbers.append(h3)

    global M_14; global M_16
    H = numbers.count(2)

    if H >= 2:
        M_14 += 2
    else:
        M_16 += 2


# 开始
start()
# 结束
done()