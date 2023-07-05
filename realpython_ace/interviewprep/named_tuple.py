"""
Named tuple
"""
from collections import namedtuple

# under the hood the second argument will call .split(" ")
car = namedtuple("Car", "color make model mileage")

my_car = car("Midnight silver", "tesla", "model y", 5)

my_car = car(color="Midnight silver", make="tesla", model="model y", mileage=5)
print(my_car)
print(isinstance(my_car, car))
