class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        tMap = Counter(t)
        sMap = {}
        have, need = 0, len(tMap)
        res, resLen = (-1, -1), float("inf")
        l = 0
        for r in range(len(s)):
            sMap[s[r]] = sMap.get(s[r], 0) + 1
            if s[r] in tMap and sMap[s[r]] == tMap[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = (l, r)
                    resLen = r - l + 1
                sMap[s[l]] -= 1
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
        l, r = res 
        return s[l: r + 1] if resLen != float("inf") else ""