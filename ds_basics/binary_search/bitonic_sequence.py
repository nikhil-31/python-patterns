

def find_highest_number(nums):

    low = 0
    high = len(nums) - 1

    if len(nums) < 3:
        return None


    while low <= high:

        mid = (low + high) // 2

        mid_left = nums[mid - 1] if mid - 1 >= 0 else float("-inf")
        mid_right = nums[mid + 1] if mid + 1 < len(nums) else float("inf")

        if nums[mid] > mid_left and nums[mid] < mid_right:
            low = mid + 1
        elif nums[mid] < mid_left and nums[mid] > mid_right:
            high = mid - 1
        elif nums[mid] > mid_left and nums[mid] > mid_right:
            return nums[mid]
    return None



A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 2, 3, 4, 5]
print(find_highest_number(A))
A = [5, 4, 3, 2, 1]
print(find_highest_number(A))
