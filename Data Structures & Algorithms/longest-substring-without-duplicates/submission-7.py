"""
Given a string s, find the length of the longest substring w/out duplicate chatacters

Ex1: s = "zxyzxyz" -> 3 (xyz)
Ex2: s = "xxxx" -> 1 (x)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        longest = 0
        matches = {}
        for r in range(len(s)):
            if s[r] in matches and matches[s[r]] >= l:
                l = matches[s[r]] + 1
            matches[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest