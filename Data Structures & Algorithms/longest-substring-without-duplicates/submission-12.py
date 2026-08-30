class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        matches = {}
        longest = 0
        l = 0
        for r in range(len(s)):
            if s[r] in matches and matches[s[r]] >= l:
                print(f"Condition triggered at idx {r}")
                l = matches[s[r]] + 1
            
            matches[s[r]] = r
            longest = max(longest, r - l + 1)
            print(matches)
            print(f"L = {l}")
        return longest