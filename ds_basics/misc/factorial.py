
def factorial(n: int):
    fact = 1
    for i in range(n):
        fact += fact * i
    return fact


print(factorial(5))




