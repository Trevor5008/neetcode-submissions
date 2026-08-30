class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = {}
        for word in strs:
            curr = [0] * 26
            for char in word:
                curr[ord(char) - ord('a')] += 1
            curr = tuple(curr)
            if curr in strMap:
                strMap[curr].append(word)
            else:
                strMap[curr] = [word]
        return [lsts for lsts in strMap.values()]