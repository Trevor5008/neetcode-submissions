"""
Given a string s, find the length of the longest substring w/out duplicate characters

Ex1: s = "zxyzxyz" -> 3 (xyz is the longest before repeating)
Ex2: s = "xxxx" -> 1 (x is the only unique character)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        res, l = 0, 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]]+1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res
