"""
Given a string 's', return true if the 's' can be a palindrome after deleting at most
one character from it

Ex1: s = "aca" -> true
Ex2: s = "abbadc" -> false (even after deleting a character, still not a palindrome)
Ex3: s = "abbda" -> true (after deleting 'd', becomes a palindrome)
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                leftSkip = s[l+1:r+1] == s[r:l:-1]
                rightSkip = s[l:r] == s[r-1:l-1:-1]
                return leftSkip or rightSkip
            l, r = l+1, r-1
        return True
