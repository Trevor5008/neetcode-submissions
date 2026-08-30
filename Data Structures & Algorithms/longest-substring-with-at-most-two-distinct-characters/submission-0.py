class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0
        longest = 0
        charMap = {}
        l = 0
        for r in range(len(s)):
            currChar = s[r]
            charMap[currChar] = charMap.get(currChar, 0) + 1
            while len(charMap) > 2:
                leftChar = s[l]
                charMap[leftChar] -= 1
                if charMap[leftChar] == 0:
                    del charMap[leftChar]
                l += 1
            longest = max(longest, r - l + 1)

        return longest