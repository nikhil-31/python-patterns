"""
link: https://leetcode.com/problems/is-subsequence/?envType=study-plan&id=level-1

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting 
some (can be none) of the characters without disturbing the relative positions of the remaining 
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to
check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""
## Recursive solution

def find_subsequence(source: str, target: str):
    LEFT_BOUND = len(source)
    RIGHT_BOUND = len(target)
   
    def rec_subsequence(left_index, right_index):
        if left_index == LEFT_BOUND:
            return True
        elif right_index == RIGHT_BOUND:
            return False

        if source[left_index] == target[right_index]:
            left_index += 1
        right_index += 1
        
        return rec_subsequence(left_index, right_index)

    return rec_subsequence(0, 0)

print(find_subsequence("abc", "ahbgcc"))

### Iterative solution

def find_iterative(source: str, target: str):
    LEFT_BOUND = len(source)
    RIGHT_BOUND = len(target)


    left_index = 0
    right_index = 0
    
    while(left_index <= LEFT_BOUND and right_index <= RIGHT_BOUND):
        if left_index == LEFT_BOUND:
            return True
        elif right_index == RIGHT_BOUND:
            return False
        
        if source[left_index] == target[right_index]:
            left_index += 1
        right_index +=1

# print(find_iterative("abc", "ahbgcc"))
