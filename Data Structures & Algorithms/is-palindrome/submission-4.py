class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(' ','')
        left, right = 0, len(s)-1
        while left < right:
            while not self.isAlphaNum(s[left]) and left < right:
                left += 1
            while not self.isAlphaNum(s[right]) and right > left:
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def isAlphaNum(self, c: chr) -> bool:
        return (ord('a') <= ord(c) <= ord('z')
                or ord('0') <= ord(c) <= ord('9'))