### Learning the difference between sort and sorted

numbers = [6,9,3,1]
print(sorted(numbers))

### The output from the sorted built in method is a new list

### Sorted can be used on tuples and sets as well, but the return value is a list
numbers_tuple = (6, 9, 3, 1)
numbers_set = {5, 5, 10, 1, 0}
numbers_tuple_sorted = sorted(numbers_tuple)
numbers_set_sorted = sorted(numbers_set)

print(numbers_tuple_sorted)

print(numbers_set_sorted)

### The returned object can be cast back to the input type
print(tuple(numbers_set_sorted))

print(set(numbers_tuple_sorted))


### Sorted strings

string_number_value = '34521'

string_value = 'I like to sort'

sorted_string_number = sorted(string_number_value)

sorted_string_value = sorted(string_value)

print(sorted_string_number)

## TO sort letters we can use split and join

str_value = 'I like to sort'

sorted_string_list = sorted(str_value.split())

sorted_string = ' '.join(sorted_string_list)
print(sorted_string)

### mixed lists can be cast to the same type
mixed_numbers = [5, "1" , 100, "200"]
print([int(x) for x in mixed_numbers])

### A list that can be converted to booleans
similar_values = [False, 0, 1, 'A' == 'B', 1 <= 0]
print(sorted(similar_values))

### While sorting the case matters, python uses unicode code point which can be 
### accessed by the ord() builtin method 
names_with_case = ['harry', 'Suzy', 'al', 'Mark']
print(sorted(names_with_case))

### The ord values
ord_list = [(ord(name[0]), name[0]) for name in sorted(names_with_case)]
print(ord_list)

### Using sorted with a reverse argument
names = ['Harry', 'Suzy', 'Al', 'Mark']

sorted(names)

print(sorted(names, reverse=True))

### sorted() with a key argument

words = ['banana', 'pie', 'Washington', 'book']
sorted_by_len_list = sorted(words, key=len)
print(sorted_by_len_list)

### Ordering by the last word

def reverse_word(word):
    return word[::-1]

words = ['banana', 'pie', 'Washington', 'book']
sorted(words, key=reverse_word)

### ORdering values with .sort()
### It is a method on the list class, it is not a built in

values_to_sort = [5, 2, 6, 1]
print(values_to_sort.sort())

from collections import namedtuple

Runner = namedtuple('Runner', 'bibnumber duration')

runners = []
runners.append(Runner('2528567', 1500))
runners.append(Runner('7575234', 1420))
runners.append(Runner('2666234', 1600))
runners.append(Runner('2425234', 1490))
runners.append(Runner('1235234', 1620))
# Thousands and Thousands of entries later...
runners.append(Runner('2526674', 1906))

runners.sort(key=lambda x: getattr(x, 'duration'))
