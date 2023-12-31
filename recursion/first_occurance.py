

def first_occ(numbers, target):


    for index, value in enumerate(numbers):
        if value == target:
            return index


arr = [9, 8, 1, 8, 1, 7]
testVariable = 1
currentIndex = 0

print(first_occ(arr, testVariable))


def first_index_recursively(numbers, target, current_index):
    if len(numbers) == current_index:
        return -1
    
    if numbers[current_index] == target:
        return current_index
    
    return first_index_recursively(numbers, target, current_index + 1)

arr = [9, 8, 1, 8, 1, 7]
testVariable = 1
currentIndex = 0

print(first_index_recursively(arr, testVariable, currentIndex))