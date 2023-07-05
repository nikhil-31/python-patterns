"""
Primer on decorators
https://realpython.com/primer-on-python-decorators/#functions
"""
from decoratorss import do_twice, timer, debug
from dataclasses import dataclass

def my_decorator(func):
    """
    Simple decorator
    """
    def wrapper():
        print("Executing something before the function")
        func()
        print("executing something after the function")
    return wrapper


def say_whee():
    """
    Killer bee
    """
    print("WHEEE")

say_whee = my_decorator(say_whee)
say_whee()

# Using the pie syntax

@my_decorator
def say_whee33333():
    """
    Killer beeeê33333
    """
    print("WHEEE3333333")

say_whee33333()


@do_twice
def say_9_tails():
    """
    Killer beeeê33333
    """
    print("Kurama")

say_9_tails()

@do_twice
def return_greeting(name):
    """
    Do twice
    """
    print("Creating greeting")
    return f"Hi {name}"

return_greeting("Adam")

@timer
def waste_some_time(num_times):
    """
    Function to waste some time
    """
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(123)

class TimeWaster:
    """
    Class to waste time
    """
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        """
        For loop to waste time
        """
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])

@dataclass
class PlayingCard:
    """
    Data class from python 3.7
    """
    rank: str
    suit: str

# Stacking decorators
@debug
@do_twice
def greet(name):
    """
    Stacked/ nested decorators
    Effectively, this is debug(do_twice(greet()))
    """
    print(f"Hello {name}")

greet("Eva")

#### CLASS Decorators
### Recall that the decorator syntax @my_decorator is just an easier way of
# saying func = my_decorator(func). Therefore, if my_decorator is a class,
# it needs to take func as an argument in its .__init__() method. Furthermore,
# the class instance needs to be callable so that it can stand in for the decorated function
### For a class instance to be callable, you implement the special .__call__() method:
class Counter:
    """
    Class to count the number of calls
    """
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        print(f"Current count is {self.count}")

counter = Counter()
counter()
counter()

print(counter.count)
