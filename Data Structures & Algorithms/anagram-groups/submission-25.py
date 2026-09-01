class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            strMap = [0]*26
            for char in word:
                strMap[ord(char) - ord('a')] += 1
            strTup = tuple(strMap)
            if strTup in groups:
                groups[strTup].append(word)
            else:
                groups[strTup] = [word]
        return [lst for lst in groups.values()]