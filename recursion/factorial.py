from timeit import timeit
# Recursively 
def factorial(n):
    print(f"factorial() called with n = {n}")
    return_value = 1 if n <= 1 else n * factorial(n -1)
    print(f"-> factorial({n}) returns {return_value}")
    return return_value

print(factorial(4))

# Iteratively 

def factorial_iterative(n):
    return_value = 1
    if n >= 1:
        while n >= 1:
            return_value = n * return_value
            n = n - 1
    return return_value

print(factorial_iterative(4))


setup_string = """
print("Recursive:")
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
"""

# print(timeit("factorial(4)", setup=setup_string, number=10000000))

# factorial is part of the math module
from math import factorial
print(factorial(4))
