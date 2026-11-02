class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        max_f, longest, l = 0, 0, 0
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            max_f = max(max_f, chars[s[r]])
            if (r - l + 1) - k > max_f:
                chars[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest