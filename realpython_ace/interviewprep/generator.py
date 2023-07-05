"""
Generators
They are special because they are lazily evaluated, they are pretty awesome actually.
We can access the values in constant time.
"""
import sys

g = (i for i in range(6))

# Printing the object
print(g)

# Printing the values in the generators
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# Trying to access the next value after all values are removed from a generator, will lead 
# to an exception `StopIteration` being thrown.
# print(next(g))

# Summing all the elements in a list
print(sum([i for i in range(1, 1001)]))

# Summing with generator
print(sum((i for i in range(1, 1001))))

# Using an iterator with a generator
iterator = iter((i for i in range(1, 1001)))

# we can call next on an iterator
print(next(iterator))

# Checking the size of a list and then generator
lst = [i for i in range(1, 1001)]

print(sys.getsizeof(lst))

gen = (i for i in range(6))
print(sys.getsizeof(gen))

# Generator function
def f():
    yield 1
    yield 2
    yield 3

# to loop through the entire
g2 = f()
print(next(g2))
print(next(g2))
print(next(g2))
