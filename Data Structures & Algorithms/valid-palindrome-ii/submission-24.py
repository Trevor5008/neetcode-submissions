class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # Try removing s[r] or s[l]
                case1 = s[l:r]
                case2 = s[l+1:r+1]
                return case1 == case1[::-1] or case2 == case2[::-1]
            l += 1
            r -= 1
        return True