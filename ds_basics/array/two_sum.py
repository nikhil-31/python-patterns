



def two_sum_hash_table(nums, target):
    dt = dict()

    for num in nums:

        if num in dt:
            print(num, dt[num])
            return True
        else:
            dt[target - num] = num
    return False

A = [-2, 1, 2, 4, 7, 11]
target = 11

print(two_sum_hash_table(A,target))



def two_sum_two_pointers(nums, target):
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] + nums[j] == target:
            print(nums[i], nums[j])
            return True
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j += 1
    return False

A = [-2, 1, 2, 4, 7, 11]
target = 12

print(two_sum_hash_table(A,target))
