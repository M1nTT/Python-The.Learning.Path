# ex5.2.py
# 试着使用变量将英寸和磅转换成厘米和千克。不要直接键入答案，使用 python 的数学计算功能来完成。

# round() 函数可以将浮点数四舍五入

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 * 2.5 # inches * 2.5 -> cm
my_weight = round(180 * 0.4536) # lbs * 0.4536 -> kg
my_eyes = 'blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} cm tall.")
print(f"He's {my_weight} kg heavy.")
print("Actually that's not too heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")