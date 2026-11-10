class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        charMap = {}
        for i in range(len(s)):
            charS = ord(s[i].lower()) - ord('a')
            charT = ord(t[i].lower()) - ord('a')
            if charS not in charMap:
                if charT in charMap.values(): return False
                charMap[charS] = charT
            elif charMap[charS] != charT: return False
        return True