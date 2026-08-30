class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest, counts = 0, {}
        l, max_f = 0, 0
        for r in range(len(s)):
            # Update current char count
            counts[s[r]] = counts.get(s[r], 0) + 1
            # Re-evaluate max frequency
            max_f = max(max_f, counts[s[r]])
            # shrink window while width > # replacements, max char count
            while (r - l + 1) > k + max_f:
                counts[s[l]] -= 1
                l += 1
            # Re-evaluate longest
            longest = max(longest, r - l + 1)
        return longest