class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        matches = {}
        l = 0
        for r in range(len(s)):
            if s[r] not in matches or matches[s[r]] < l:
                matches[s[r]] = r
            else:
                l = matches[s[r]] + 1
                matches[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest