"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23
"""

def max_sub_array(numbers):
    """
    Program that calculates the maximum subarray
    :param numbers - list of integers
    :return - The sum of the maximum subarray
    """
    current_subarray = max_subarray = nums[0]

    for num in numbers[1:]:
        current_subarray = max(num, current_subarray + num)
        max_subarray = max(max_subarray, current_subarray)
    return max_subarray

nums = [5,4,-1,7,8]
print(max_sub_array(nums))
