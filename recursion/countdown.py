"""
Countdown using recursive and iterative approach
"""
def countdown(num):
    """
    Recursive countdown
    """
    print(num)
    if num == 0:
        return             # terminate recursion
    else:
        countdown(num - 1)   # Recursion call

#countdown(100)
def countdown_2(num):
    """
    Recursive countdown
    """
    print(num)
    if num > 0:
        countdown_2(num - 1)

countdown_2(100)

# iterative
def countdown_3(num):
    """
    Iterative countdown
    """
    print(num)
    while num >= 0:
        num -= 1

countdown_3(50)
