class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = {}
        for st in strs:
            key = "".join(sorted(st))
            if key in strMap:
                strMap[key].append(st)
            else:
                strMap[key] = [st]
        return list(strMap.values())