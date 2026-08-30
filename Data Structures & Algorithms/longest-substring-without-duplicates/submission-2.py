class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        maxLen = 0
        seen = ""
        l, r = 0, 0
        while r < len(s):
            if s[r] not in seen:
                seen += s[r]
                maxLen = max(maxLen, len(seen))
                r += 1
            else: 
                l += 1
                seen = s[l:r]
        return maxLen