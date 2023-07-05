"""
sorted method leaves the original list alone, it will create a new list
"""

animals = ["cat", "dog", "cheetah", "rhino"]
animals_sorted = sorted(animals)
print(animals_sorted)


animals = [
    {"type": 'cat', 'name': 'steph', 'age': 8},
    {"type": 'dog', 'name': 'kekw', 'age': 9},
    {"type": 'homan', 'name': 'opo', 'age': 22},
]

dict_sorted = sorted(animals, key=lambda animal: animal.get('age'))
print(dict_sorted)
