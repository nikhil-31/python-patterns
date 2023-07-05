"""
f strings are called formatted string literals
This is only present on python 3.6 and above, 
Do not use this for user inputs
"""

name = 'nikhil'
age = 5

print("My name is {}.".format(name))

# Using f strings
print(f"My name is {name}. Using an f-string")

print(f"My name is {name}, and my age is {age +5} year old.")


class A(object):

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return (
            f"My name is {self.name} \n"
            f"My age is {self.age}"
        )

a = A('nikhil', 3)
print(a)
