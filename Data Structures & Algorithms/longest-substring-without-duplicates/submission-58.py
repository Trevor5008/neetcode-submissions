class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        longest = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in chars or chars[s[r]] < l:
                chars[s[r]] = r
                longest = max(longest, r - l + 1)
            elif s[r] in chars and chars[s[r]] >= l:
                l = chars[s[r]] + 1
                chars[s[r]] = r
        return longest