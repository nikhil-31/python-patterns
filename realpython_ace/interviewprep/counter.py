from collections import defaultdict, Counter


def top_three_letters(string):
    """
    This method will return the top 3 most
    repeated letters in a string,
    Returns a list of tuples, where tuple
    contains the charcters

    >>> top_three_letters("abbccc")
    [('c': 3), ('b': 2), ('a': 1)]
    """
    # loop through the string and store the count for each letter
    # sort the dict by the count and find the top 3 frequent letters
    # return formatted list with the output

    counter = defaultdict(int)
    for c in string:
        counter[c] += 1
    top_three = sorted(counter, key=lambda k: counter[k], reverse=True)[:3]
    return [(letter, counter[letter]) for letter in top_three]


def top_three_letter_counter(string):
    """
    This method will return the top 3 most
    repeated letters in a string,
    Counter is a subclass of dict for counter hashable items

    >>> top_three_letter_counter("abbccc")
    [('c': 3), ('b': 2), ('a': 1)]
    """
    top_three = Counter(string).most_common(3)
    print(top_three)
