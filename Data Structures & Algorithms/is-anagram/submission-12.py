class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lenS, lenT = len(s), len(t)
        if lenS != lenT: return False
        sMatches, tMatches = [0]*26, [0]*26
        for i in range(len(s)):
            sMatches[ord(s[i]) - ord('a')] += 1
            tMatches[ord(t[i]) - ord('a')] += 1
        
        return tMatches == sMatches