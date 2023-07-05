"""
link: https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan&id=level-1

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""

def isomorphic_strings(s: str, t: str) -> bool:
    return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

print(isomorphic_strings("paper", "title"))