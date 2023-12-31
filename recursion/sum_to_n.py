

def sum_to_n(nums):

    if nums == 1:
        return nums
    
    return nums + sum_to_n(nums - 1)

targetNumber = 5
print(sum_to_n(targetNumber))