class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            wordKey = "".join(map(str, sorted(word)))
            if wordKey in anagrams:
                anagrams[wordKey].append(word)
            else:
                anagrams[wordKey] = [word]
        return list(anagrams.values())