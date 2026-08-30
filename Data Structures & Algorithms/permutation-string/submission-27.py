"""
Given two strings s1 and s2
return True if s2 contains a permutation of s1, or False otherwise

Ex1: s1 = "abc", s2 = "lecabee" -> True (cab == abc)
Ex2: s1 = "abc", s2 = "lecaabee" -> False (caab != abc)
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0]*26, [0]*26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            print(f"Matches at index {r} = {matches}")
            if matches == 26: 
                return True

            idx = ord(s2[r]) - ord('a')
            s2Count[idx] += 1
            if s2Count[idx] == s1Count[idx]:
                matches += 1
            elif s1Count[idx] + 1 == s2Count[idx]:
                matches -= 1

            idx = ord(s2[l]) - ord('a')
            s2Count[idx] -= 1
            if s2Count[idx] == s1Count[idx]:
                matches += 1
            elif s1Count[idx] - 1 == s2Count[idx]:
                matches -= 1
            l += 1
        return matches == 26