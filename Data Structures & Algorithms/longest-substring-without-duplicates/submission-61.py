class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars, longest, l = {}, 0, 0
        for r in range(len(s)):
            if s[r] in chars and chars[s[r]] >= l:
                l = chars[s[r]] + 1
            chars[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest