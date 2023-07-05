def func():
    print("I am a function")

func()

another_name = func
another_name()

print(["cat", func, 42])

objects = ["cat", func, 42]


def outer():
    def inner():
        print("The inner function")
    return inner

function = outer()
function()

# Lambda expression - Assigned to a variable
a = lambda x: x * x 
print(a(2))

(lambda s: s[::-1])("I am a string")


def reverse(s):
    return s[::-1]

animals = ['ferret', 'vole', 'dog', 'gecko']

def reverse_len(s):
    return -len(s)

reverse_len(animals)

print(-len('asvd'))

print(sorted(animals, key=lambda x: -len(x)))

forty_two_producer = lambda: 42
print(forty_two_producer())

"""
********* MAP DOES NOT RETURN A LIST IT RETURNS AN ITERATOR, use the list() method 
"""
print(list(map(lambda s: s[::-1], animals)))


# Joining a list of integers that are convereted to strings
str_list = list()
for i in [1, 2, 3, 4, 5]:
    str_list.append(str(i))

print(str_list)

"+".join(str_list)

print("+".join(map(lambda s: str(s) , [1,2,3,4,5] )))

### Passing multiple lists into map

print(list(
    map(
        (lambda a, b, c: a + b + c),
        [1, 2, 3],
        [10, 20, 30],
        [100, 200, 300]
    )
))

print(list(map(lambda s: s > 100, [1, 1000, 2])))

print(list(filter(lambda s:s > 100, [1, 1000, 2])))

# Is even

print(list(filter(lambda x: x % 2 == 0, range(10))))

print(list(filter(lambda x: x % 2 == 0, range(1000))))

print(list(filter(lambda s: s.isupper(), ['abc', 'ABC'])))

# Reducing the iterable to a single value

from functools import reduce

def f(x, y):
    return x + y

print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))

print(reduce(lambda x, y: x+y, ['asdf', 'asdfd', 'asdfsaw']))

"".join(["Asdf","asdfd", "Asdfas"])

# Finding the maximum value in a list
max([123, 1232])

def greater(x, y):
    return x if x > y else y

from functools import reduce
print(reduce(greater, [12,23,2321,23]))


def factorial(n):
    from functools import reduce
    return reduce(lambda x, y: x * y, range(1, n + 1))

print(dir(__builtins__))

sum(i * i for i in range(1000000000))
