class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        window = defaultdict(int)
        have, need = 0, len(countT)

        res, resLen = "", float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]
                
                left = s[l]
                window[left] -= 1
                if left in countT and window[left] < countT[left]:
                    have -= 1
                l += 1

        return res