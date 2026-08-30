class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        longest = 0
        charMap = {}
        for r in range(len(s)):
            currChar = s[r]
            if currChar in charMap and charMap[currChar] >= l:
                l = charMap[currChar] + 1
            else:
                longest = max(longest, r - l + 1)
            charMap[currChar] = r
        return longest