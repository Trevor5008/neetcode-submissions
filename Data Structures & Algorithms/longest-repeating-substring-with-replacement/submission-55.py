class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts, longest = {}, 0
        max_f, l = 0, 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            max_f = max(max_f, counts[s[r]])
            while (r - l + 1 - max_f) > k:
                counts[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest