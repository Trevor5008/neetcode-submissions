"""
Given two strings s1 and s2,
return true if s2 contains a permutation of s1 (false otherwise)

Ex1: s1 = "abc", s2 = "lecabee" -> True ('cab' inside s2)
Ex2: s2 = "abc", s2 = "lecaabee" -> False
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        matches = 0
        s1Count, s2Count = [0]*26, [0]*26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
        
            # Gaining a character as r moved right
            idx = ord(s2[r]) - ord('a')
            s2Count[idx] += 1
            if s1Count[idx] == s2Count[idx]:
                matches += 1
            elif s1Count[idx] + 1 == s2Count[idx]:
                matches -= 1

            # Losing a character as l moved right
            idx = ord(s2[l]) - ord('a')
            s2Count[idx] -= 1
            if s1Count[idx] == s2Count[idx]:
                matches += 1
            elif s1Count[idx] - 1 == s2Count[idx]:
                matches -= 1
            l += 1
        return matches == 26