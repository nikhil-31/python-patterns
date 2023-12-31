

def binary_seach_rotated(nums, target):

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:
            if nums[low] <= target and target < nums[mid]:
                high = mid - 1 
            else:
                low = mid + 1 
        else:
            if nums[mid] < target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1 
    return -1


nums_list = [[5, 6, 7, 1, 2, 3, 4],
                [40, 50, 60, 10, 20, 30],
                [47, 58, 69, 72, 83, 94, 12, 24, 35], 
                [77, 82, 99, 105, 5, 13, 28, 41, 56, 63], 
                [48, 52, 57, 62, 68, 72, 5, 7, 12, 17, 21, 28, 33, 37, 41]]

target_list = [1, 50, 12, 56, 5]

for i in range(len(target_list)):
    print((i + 1), ".\tRotated array: ", nums_list[i], "\n\ttarget", target_list[i], "found at index ", \
            binary_seach_rotated(nums_list[i], target_list[i]))
    print("-"*100)








