# 循环和列表

# range(0, 6) 函数：会从第一个数数到最后一个数，但不包含最后一个数。都是整数。
# list1.append(list2) 函数：在一个列表(list1)的尾部追加另一个列表(list2)
# for…A…in…B… 语法：将B列表中的元素赋予给列表A

the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes throught a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(F"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was : {i}")
