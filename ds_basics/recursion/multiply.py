

def recursive_multiply(x, y):

    if x < y:
        return recursive_multiply(y, x)

    if y == 0:
        return 0
    
    return x + recursive_multiply(x, y - 1)


