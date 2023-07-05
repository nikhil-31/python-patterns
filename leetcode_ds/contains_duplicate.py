"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
nums = [1,1,1,3,3,4,3,2,4,2]

###############################
# Solution 1: Using dictionary
###############################
def contains_duplicate(nums) -> bool:
    """
    Checks if an array contains a duplicate using a for loop
    """
    dupl_dict = dict()
    for number in nums:
        if number in dupl_dict:
            return True
        else:
            dupl_dict[number] = 1
    return False

print(contains_duplicate(nums))

###############################
# Solution 2: Using set
###############################
def contains_duplicate_set(nums) -> bool:
    """
    Checks if an array contains a duplicate using the len function
    """
    return len(set(nums)) < len(nums)

print(contains_duplicate_set(nums))
