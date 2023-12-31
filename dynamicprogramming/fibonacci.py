


def fibonacci(n):
    a = 0
    b = 1

    if n < 0:
        print('Invalid input')
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            temp = a + b
            a = b
            b = temp
        return b
    
print(fibonacci(9))
