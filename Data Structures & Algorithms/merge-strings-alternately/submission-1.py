class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        m, n = len(word1), len(word2)
        newWord = ""

        while i < m and j < n:
            newWord = newWord + word1[i] + word2[j]
            i, j = i + 1, j + 1

        if i < m:
            newWord += word1[i:m+1]
        elif j < n:
            newWord += word2[j:n+1]
        return newWord