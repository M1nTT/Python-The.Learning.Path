# ex30.1.py
# 试着写一些复杂的布尔表达式，如 cars > people or trucks < cars


people = 30
cars = 40
trucks = 15


if cars + trucks > people:
    print("Lack of adequate drivers.")
elif cars + trucks < people:
    print("There are enough drivers.")
else:
    print("Just right.")

if trucks * 2 + cars * 4 > people:
    print("There are enough seats for people to do.")
elif trucks * 2 + cars * 4 < people:
    print("There are not enough seats for people to do.")
else:
    print("Just right.")

if people > cars and people > trucks and people > 5:
    print("There are more people than cars and more trucks, and the sum of the number of cars and trucks must be greater than 5.")
else:
    print("The number of people is greater than the car, the number of people is greater than the truck, and the number of people is greater than 5, will not be true at the same time.")