

def find_square(num):
    return num * num


def find_square_recursively(num):
    if num == 0:
        return 0
    return find_square_recursively(num - 1) + (2 * num) - 1


targetNumber = 5
print(find_square(targetNumber))
print(find_square_recursively(targetNumber))