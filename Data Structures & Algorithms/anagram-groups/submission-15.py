class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return []
        strMap = {}
        for word in strs:
            keyMap = [0] * 26
            for char in word:
                keyMap[ord(char) - ord('a')] += 1
            keyMap = tuple(keyMap)
            if keyMap in strMap:
                strMap[keyMap].append(word)
            else:
                strMap[keyMap] = [word]
        return [lst for lst in strMap.values()]