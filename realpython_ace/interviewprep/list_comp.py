"""
List compherension
"""

lst = [1,2,-3,1]

def square(num):
    """
    Returns the square of a number
    :param x - number
    :return - number
    """
    return num * num

print(map(square, lst))

print([square(val) for val in lst  ])

print([(lambda x: x % 2)(num) for num in lst])
