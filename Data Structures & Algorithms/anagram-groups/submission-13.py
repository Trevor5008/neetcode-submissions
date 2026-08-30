class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return []
        strMap = {}
        for word in strs:
            keyWord = "".join(sorted(word))
            if keyWord in strMap:
                strMap[keyWord].append(word)
            else:
                strMap[keyWord] = [word]
        return [lst for lst in strMap.values()]