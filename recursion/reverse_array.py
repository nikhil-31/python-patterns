

def reverse(array):

    if array == []:
        return []
    
    elif len(array) == 1:
        return array
    
    else:
        return [array[-1]] + reverse(array[:-1])

array = [1, 2, 3, 4]
print(reverse(array))
