# From ex19.2.py
# Calculating definite integrals

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