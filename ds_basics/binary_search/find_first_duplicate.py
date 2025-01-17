

def first_duplicate(A, target):

    low = 0
    high = len(A) - 1


    while low <= high:
        mid = (low + high) // 2

        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            elif A[mid - 1] != target:
                return mid
            high = mid - 1

    return None

A = [-14, -10, 2, 102, 108, 243, 285, 285, 285, 401]
target = 108
x = first_duplicate(A, target)
print(x)
        


