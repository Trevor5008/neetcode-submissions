"""
Given two strings s1 and s2,
return true if s2 contains a permutation of s1 (false otherwise)

Ex1: s1 = "abc", s2 = "lecabee" -> True ('cab' inside s2)
Ex2: s2 = "abc", s2 = "lecaabee" -> False
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        l, r = 0, len(s1)-1
        s1 = sorted(s1)
        while r < len(s2):
            if s1 == sorted(s2[l:r+1]):
                return True
            l, r = l + 1, r + 1
        return False
        