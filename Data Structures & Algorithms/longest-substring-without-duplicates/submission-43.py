class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        l, r = 0, 0
        longest = 0

        while l <= r and r < len(s):
            currChar = s[r]
            if currChar not in charMap or charMap[currChar] < l:
                charMap[currChar] = r
                longest = max(longest, r - l + 1)
            else:
                l = charMap[currChar] + 1
                charMap[currChar] = r
            r += 1
            print(charMap)
        return longest