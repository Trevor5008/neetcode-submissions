class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        longest = 0
        charMap = {}
        for r in range(len(s)):
            currChar = s[r]
            if currChar in charMap and charMap[currChar] >= left:
                left = charMap[currChar] + 1
            else:
                longest = max(longest, r - left + 1)
            charMap[currChar] = r
        return longest