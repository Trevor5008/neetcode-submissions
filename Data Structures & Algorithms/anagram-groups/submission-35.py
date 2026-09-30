from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)
        for st in strs:
            key = [0]*26
            for c in st:
                key[ord(c) - ord('a')] += 1
            strMap[tuple(key)].append(st)
        return list(strMap.values())