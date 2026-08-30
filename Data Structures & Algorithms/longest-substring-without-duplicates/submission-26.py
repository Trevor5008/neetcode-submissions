class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest = 0
        charMap = {}
        while right < len(s):
            currChar = s[right]
            if currChar in charMap and charMap[currChar] >= left:
                left = charMap[currChar] + 1
                charMap[currChar] = right
            else:
                charMap[currChar] = right
                longest = max(longest, right - left + 1)
            right += 1
        return longest