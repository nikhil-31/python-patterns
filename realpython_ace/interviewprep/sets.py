#####################################################
# Command to run doctest `python3 -m doctest sets.py`
#####################################################

def count_unique_list(input_str: str):
    '''
    Count the number of unique characters in a string

    >>> count_unique_list("aabb")
    2
    >>> count_unique_list("abcdef")
    6
    '''

    seen_c = list() # O(n)
    for instance in input_str: # O(n)
        # The line below will loop through the entire list in the worst case
        if instance not in seen_c: # O(n)
            seen_c.append(instance) # O(1)

    return len(seen_c) # O(n * n) = O(n^2)

def count_unique_set(s):
    '''
    Count the number of unique characters in a string
    >>> count_unique_set("aabb")
    2
    >>> count_unique_set("abcdef")
    6
    '''
    seen_c = set()
    for c in s:
        if c not in seen_c:
            seen_c.add(c)
    return len(seen_c)

print("Printing the output")
print(count_unique_list('askdfhskhd'))


def count_unique_set_fancy(s):
    '''
    Count the number of unique characters in a string
    >>> count_unique_set_fancy("aabb")
    2
    >>> count_unique_set_fancy("abcdef")
    6
    accessing a set is O(1)
    '''

    # return len({c for c in s})
    return len(set(s))

print("Printing the output")
print(count_unique_set_fancy('askdfhskhd'))
