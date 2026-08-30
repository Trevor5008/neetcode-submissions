class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        l = 0
        longest = 0
        for r in range(len(s)):
            currChar = s[r]
            if currChar not in charMap or charMap[currChar] < l:
                charMap[s[r]] = r
            elif currChar in charMap and charMap[currChar] >= l:
                l = charMap[currChar] + 1
                charMap[currChar] = r
                r = l 
            longest = max(longest, r - l + 1)
        return longest