"""
When you compare charaters in python it compares the ascii value of the string
"""
import string
import timeit
print(ord('A'))
print(ord('a'))

'A' > 'a'

print('Hello WOrld'.isupper())
print(string.ascii_uppercase)

# Ascii uppercase set
def is_upper(s):
    for letter in s:
        if letter not in string.ascii_uppercase:
            return False
    return True


def is_upper_using_set(s):
    uppercase_set = set(string.ascii_uppercase)
    for letter in s:
        if letter not in uppercase_set:
            return False
    return True

print(is_upper('ABC'))

print(is_upper('abc'))

# print(timeit.timeit(is_upper('abc')))
# Removing all whitespaces

def remove_whitespace(word):
    whitespace_set = string.whitespace
    return ''.join(letter for letter in word if letter not in whitespace_set)

print(remove_whitespace("HELLO WORLD"))