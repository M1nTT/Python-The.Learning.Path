# ex19.1.py
# 倒着将脚本读完，在每一行上面添加一条注释，说明这一行的作用。

# 定义函数cheese_and_crackers,参数分别是cheese_count和boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # 打印格式化字符串
    print(f"You have {cheese_count} cheeses!")
    # 打印格式化字符串
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # 打印字符串
    print("Man that's enough for a party!")
    # 打印字符串，并换行。
    print("Get a blanket.\n")


# 打印字符串
print("We can just give the function numbers directly:")
# 调用函数cheese_and_crackers，参数分别是10和30
cheese_and_crackers(20, 30)


# 打印字符串
print("OR, we can use variables from our script:")
# 将10赋值给变量amount_of_cheese
amount_of_cheese = 10
# 将50赋值给变量amount_of_crackers
amount_of_crackers = 50

# 调用函数cheese_and_crackers，参数分别是amount_of_cheese和amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# 打印字符串
print("We can even do math inside too:")
# 调用函数cheese_and_crackers，参数分别是10+20和5+6
cheese_and_crackers(10 + 20, 5 + 6)

# 打印字符串
print("And we can combine the two, variables and math:")
# 调用函数cheese_and_crackers，参数分别是amount_of_cheese + 100和amount_of_crackers + 1000
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)