# ex19.2.py
# 自己编写至少一个函数出来，然后用10种不同的方式运行这个函数。

from sympy import symbols, integrate

def Integral(function, upper_limit, lower_limit):
    print(f"\nThe desired function is: ∫ {function} dx")
    x = symbols('x')
    a = upper_limit
    b = lower_limit
    f = function
    result = integrate(f, (x, a, b))
    print(f"Result = {result}")

print("This is a python script for calculating indefinite integrals")
print("Please enter the function: ")
function = input("> ")

print("Please enter the upper limit: ", end='')
upper_limit = input(" ")

print("Please enter the lower limit: ", end='')
lower_limit = input(" ")

Integral(function, upper_limit, lower_limit)