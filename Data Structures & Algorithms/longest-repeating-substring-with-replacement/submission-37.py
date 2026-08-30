class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        left = 0
        max_f = 0
        max_len = 0
        for right in range(len(s)):
            charMap[s[right]] = charMap.get(s[right], 0) + 1
            max_f = max(max_f, charMap[s[right]])
            
            while (right - left + 1) - max_f > k:
                charMap[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        return max_len