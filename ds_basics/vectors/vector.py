

class Vector:

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except:
            raise ValueError('Coordiantes must not be empty')


    def __str__(self) -> str:
        return f"Vector: {self.coordinates}"
    

    def __eq__(self, v) -> bool:
        return self.coordinates == v.coordinates


my_vector = Vector([1, 2, 3])
print(my_vector)
my_vector2 = Vector([1, 2, 3])
print(my_vector == my_vector2)


