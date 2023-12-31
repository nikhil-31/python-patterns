


def find_fixed_point(nums):

    low = 0
    high = len(nums) - 1



    while low <= high:

        mid = (low + high) // 2

        if nums[mid] < mid:
            low = mid + 1
        elif nums[mid] > mid:
            high = mid - 1
        else:
            return nums[mid]
        
    return None


A1 = [-10, -5, 0, 3, 7]

# Fixed point is 0:
A2 = [0, 2, 5, 8, 17]

# No fixed point. Return "None":
A3 = [-10, -5, 3, 4, 7, 9]

print("Binary Search Approach")
print(A1)
print(find_fixed_point(A1))
print(A2)
print(find_fixed_point(A2))
print(A3)
print(find_fixed_point(A3))