class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest = 0
        charMap = {}
        while right < len(s):
            currChar = s[right]
            if currChar not in charMap or charMap[currChar] < left:
                charMap[currChar] = right
                longest = max(longest, right - left + 1)
            else:
                left = charMap[currChar] + 1
                charMap[currChar] = right
            right += 1
        return longest