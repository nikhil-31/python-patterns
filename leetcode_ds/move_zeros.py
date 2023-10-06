"""
Link - https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=programming-skills
"""

def move_zeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0

        for j in range(n):
            if(nums[j] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

print(move_zeroes([4,2,4,0,0,3,0,5,1,0]))
