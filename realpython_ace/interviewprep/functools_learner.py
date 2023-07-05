
from functools import reduce, lru_cache, cached_property
# cached_property can only be used above python 3.8
# Reduce an iterable into one value
print(reduce(lambda x, y : x * y, [1,2,3,4]))
print(reduce(lambda x, y: x * y, [1,2,3,4], 10))

class Data:

    def __init__(self, n) -> None:
        self.n = n


    @cached_property
    def f(self):
        total = 0
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    total += i + j + k
        return total


@lru_cache
def fibonacci(n):
    """
    0, 1, 1, 2, 3, 5
    """
    print(n)
    if n <= 1:
        return n 
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(25))    