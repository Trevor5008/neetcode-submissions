class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countMap = {}
        max_f = 0
        longest = 0
        l = 0
        for r in range(len(s)):
            countMap[s[r]] = countMap.get(s[r], 0) + 1
            max_f = max(countMap[s[r]], max_f)
            while (r - l + 1) - max_f > k:
                countMap[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest