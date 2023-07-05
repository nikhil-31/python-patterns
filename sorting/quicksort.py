
import time
import random


def quicksort(items):
    
    if(len(items) <= 1):
        return items

    pivot = random.choice(items)

    items_less_than_pivot = [x for x in items if x < pivot]
    equal_to_pivot = [x for x in items if x == pivot]
    greater_than_pivot = [x for x in items if x > pivot]

    return quicksort(items_less_than_pivot) + equal_to_pivot + quicksort(greater_than_pivot)


items = [random.randint(1, 1000) for  _ in range(10000000)]
start = time.perf_counter()

quicksort(items)

print(time.perf_counter() - start)

