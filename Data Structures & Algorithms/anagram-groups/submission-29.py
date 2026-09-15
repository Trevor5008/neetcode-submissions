class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            word = [0]*26
            for char in s:
                word[ord(char) - ord('a')] += 1
            word = tuple(word)
            if word in res:
                res[word].append(s)
            else:
                res[word] = [s]
        return list(res.values())