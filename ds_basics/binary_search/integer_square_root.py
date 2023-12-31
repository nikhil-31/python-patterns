


def integer_square_root(target):


    low = 0
    high = target

    while low <= high:

        mid = (low + high) // 2
        mid_squared = mid * mid
        
        if mid_squared <= target:
            low = mid + 1
        else:
            high = mid - 1

    return low - 1


k = 300
print(integer_square_root(k))