class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s): return False
        sMap, tMap = [0]*26, [0]*26
        for i in range(len(s)):
            sMap[ord(s[i]) - ord('a')] += 1
            tMap[ord(t[i]) - ord('a')] += 1

        return sMap == tMap