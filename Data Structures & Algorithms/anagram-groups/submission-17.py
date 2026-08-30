class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        wordsMap = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in wordsMap:
                wordsMap[key].append(word)
            else:
                wordsMap[key] = [word]
        return [lst for lst in wordsMap.values()]