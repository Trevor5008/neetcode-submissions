class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        l, r = 0, 0
        matches = 0
        while l < len(s) and r < len(t):
            print(f"l at {l}, r at {r}")
            if s[l] == t[r]:
                matches += 1
                l += 1
                r += 1
            while r < len(t) and l < len(s) and s[l] != t[r]:
                r += 1
        return True if matches == len(s) else False
            