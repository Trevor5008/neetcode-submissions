class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap, longest = {}, 0
        l = 0
        for r in range(len(s)):
            if s[r] in charMap and charMap[s[r]] >= l:
                l = charMap[s[r]] + 1
            charMap[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest