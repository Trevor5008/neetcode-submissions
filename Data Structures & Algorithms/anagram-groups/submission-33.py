from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)
        for st in strs:
            key = "".join(sorted(st))
            strMap[key].append(st)
        return list(strMap.values())