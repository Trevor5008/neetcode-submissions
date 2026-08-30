from collections import Counter
class Solution:
    # XYYX
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxFreq = 0
        count = k
        for r in range(len(s)):
            counts = Counter(s[l:r+1])
            while (len(s[l:r+1]) - counts.most_common(1)[0][1]) > k:
                l += 1 # shrink window
                counts = Counter(s[l:r+1])
            maxFreq = max(maxFreq, r - l + 1)
        return maxFreq