from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)
        for st in strs:
            key = [0]*26
            for i in range(len(st)):
                key[ord(st[i]) - ord('a')] += 1
            strMap[tuple(key)].append(st)
        return list(strMap.values())