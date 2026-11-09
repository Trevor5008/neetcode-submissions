class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        max_f = 0
        longest = 0
        l = 0
        for i in range(len(s)):
            charMap[s[i]] = charMap.get(s[i], 0) + 1
            max_f = max(max_f, charMap[s[i]])
            if l < i and (i - l + 1) - k > max_f:
                charMap[s[l]] -= 1
                l += 1
            longest = max(longest, i - l + 1)
        return longest                    