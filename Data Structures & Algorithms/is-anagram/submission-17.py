class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sMap = Counter(s)
        tMap = Counter(t)
        for key in sMap.keys():
            if tMap[key] != sMap[key]: return False
        return True