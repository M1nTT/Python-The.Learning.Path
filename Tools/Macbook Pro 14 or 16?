# Should you choose Macbook Pro 14" or 16"?

from sys import exit

# Score
M_14 = 0
M_16 = 0

prompt = "\nEnter pure numbers > "

### Part I: The beginning

def start():
    print("""
    You decide to buy a Macbook_Pro,
    But you don't know whether to choose 14 inches or 16 inches. 
    I'm going to ask you a series of questions, 
    Thus giving you the answer.
    """)

    print("Do you want to start?")
    print("1. Start")
    print("2. Exit")
    go_on = input(prompt)

    if go_on == "1":
        Q_01()
    elif go_on == "2":
        Goodbye("Okay, the program has exited...")
    else:
        Pure()
        start()



### Part II: Program Features  

# Exit
def Goodbye(why):
    print("\n", why)
    exit(0)

# Enter the prompt
def Pure():
    print("**********Typo: Please enter a pure number**********")


# Output the result
import random

def done():
    if M_14 > M_16:
        print("-------------------")
        print("End of Q&A: 14 inch is more suitable for you.")
        print("-------------------")
        exit(0)
    elif M_14 == M_16:
        M_14 + random.randint(-2,2)
        if M_14 > M_16:
            print("-------------------")
            print("End of Q&A: 14 inch is more suitable for you.")
            print("-------------------")
            exit(0)
        else:
            print("-------------------")
            print("End of Q&A: 16 inch is more suitable for you.")
            print("-------------------")
            exit(0)
    else:
        print("-------------------")
        print("End of Q&A: 16 inch is more suitable for you.")
        print("-------------------")
        exit(0)



### Part III: Questions  

# Q_01 Your gender?
def Q_01():
    print("\n")
    print("& your gender?")
    print("1. Male\n2. Female\n3. Other")

    x = input(prompt)
    global M_14; global M_16
    
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


# Q_02 What is the budget?
def Q_02():
    print("\n")
    print("& What is the budget?")
    print("1. 2000-2600 USD\n2. 2600-3200 USD\n3. 3200- USD")

    x = input(prompt)
    global M_14; global M_16
    
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


# Q_03 Does 16 inches feel oppressive for you?
def Q_03():
    print("\n")
    print("& Does 16 inches feel oppressive for you?")
    print("1. Yes\n2. No")

    x = input(prompt)
    global M_14; global M_16
    
    if x == "1":
        M_14 += 1
        Q_04()      #
    elif x == "2":
        M_16 += 1
        Q_04()
    else:
        Pure()
        Q_03()

# Q_04 Will there be an external screen?
def Q_04():
    print("\n")
    print("& Will there be an external screen?")
    print("1. Yes\n2. No")

    x = input(prompt)
    global M_14; global M_16
    
    if x == "1":
        M_14 += 1
        Q_05()
    elif x == "2":
        M_16 += 1
        Q_05()
    else:
        Pure()
        Q_04()

# Q_05 How many times a week is the average takeaway?
def Q_05():
    print("\n")
    print("& How many times a week is the average takeaway?")
    print("1. 0time\n2. 1-3time\n3. 4-7time\n4. More than 7 times")

    x = input(prompt)
    global M_14; global M_16
    
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


# Q_06 Portability
def Q_06():

    print("\n")
    print("& Commuting method")
    print("1. walk\n2. public transport\n3. bicycle\n4. automobile")
    
    y1 = int(input(prompt))

    print("\n")
    print("& Your backpack?")
    print("1. Barely fits 14 inches\n2. Easily fits 14 inches\n3. Easily fits 16 inches")

    y2 = int(input(prompt))

    print("\n")
    print("& Commuting time?")
    print("1. More than 30 minutes\n2. Less than 30 minutes\n3. No need to commute")
    
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


# Q_07 performance
def Q_07():

    numbers = []

    print("\n")
    print("& Do you often use multiple windows?")
    print("1. Yes\n2. No")
        
    h1 = int(input(prompt))
    numbers.append(h1)

    print("\n")
    print("& Do you rely on the status bar?")
    print("1. Yes\n2. No")
        
    h2 = int(input(prompt))
    numbers.append(h2)

    print("\n")
    print("& Is a high load required?")
    print("1. Yes\n2. No")
        
    h3 = int(input(prompt))
    numbers.append(h3)

    global M_14; global M_16
    H = numbers.count(2)

    if H >= 2:
        M_14 += 2
    else:
        M_16 += 2



start()

done()