"""
Given a string s, find the length of the longest substring w/out duplicate
characters.

Ex1: "zxyzxyz" -> 3
Ex2: "xxxx" -> 1
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        charMap = {}

        l = 0
        for r in range(len(s)):
            if s[r] in charMap and charMap[s[r]] >= l:
                l = charMap[s[r]] + 1
            longest = max(longest, r - l + 1)
            charMap[s[r]] = r
        return longest