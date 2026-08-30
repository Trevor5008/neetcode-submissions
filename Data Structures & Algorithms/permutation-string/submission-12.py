"""
Given two strings s1 and s2
Return true if s2 contains a permutation of s1 (false otherwise)
Basically, if a permutation of s1 exists as a substring of s2, return true
- Both strings only contain lowercase letters

Ex1: s1 = "abc", s2 = "lecabee" -> true, "cab" is in "lecabee"
Ex2: s1 = "abc", s2 = "lecaabee" -> false, no permutation of "abc" in s2 
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s1_sorted = sorted(s1)
        for i in range(0, len(s2) - s1_len + 1):
            if s1_sorted == sorted(s2[i : i + s1_len]):
                return True
        return False