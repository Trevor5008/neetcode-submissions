from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        res = ""
        need = Counter(t)
        missing = len(t)
        l, r = 0, 0
        min_len = float('inf')
        while r < len(s):
            if need[s[r]] > 0:
                missing -= 1
            need[s[r]] -= 1
            r += 1
            
            while missing == 0:
                if r - l < min_len:
                    min_len = r - l
                    res = s[l:r]
                
                need[s[l]] += 1
                if need[s[l]] > 0:
                    missing += 1
                l += 1
        return res