"""
Convert a list of tuples to a dictionary
"""
lst = [(1,0), (2,0), (3,9)]
dictionary = { l[0]: l[1] for l in lst }
print(dictionary)
