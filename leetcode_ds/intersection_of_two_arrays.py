"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays
and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such
 that you cannot load all elements into the memory at once?
"""
from collections import defaultdict

def intersection_of_two_arrays(nums1, nums2):
    """
    This method returns the intersection of two numbers
    """
    nums1_dict = defaultdict(int)
    intersection = list()

    for num in nums1:
        nums1_dict[num] = nums1_dict[num] + 1

    for num in nums2:
        if num in nums1_dict and nums1_dict[num] > 0:
            intersection.append(num)
            nums1_dict[num] = nums1_dict[num] - 1

    return intersection

nums1 = [1, 2, 3, 4, 5]
nums2 = [2, 3, 5, 4]

print(intersection_of_two_arrays(nums1, nums2))
