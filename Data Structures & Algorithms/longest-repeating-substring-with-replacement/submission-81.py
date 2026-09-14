class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        max_f = 0
        l = 0
        longest = 0
        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) + 1
            max_f = max(max_f, charMap[s[r]])
            while (r - l + 1) - max_f > k:
                charMap[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
