"""
Range - Returns the index from 0 to the number
Enumerate - Returns the index, value of a iterable
"""

def fizz_buzz(numbers):
    """
    Highlighting the difference between enumerate vs range
    """
    # This is for range
    for i in range(len(numbers)):
        print(i)

    # This is for enumerate 
    for i, value in enumerate(numbers):
        print(i, value)

fizz_buzz([1,2,2,3])
