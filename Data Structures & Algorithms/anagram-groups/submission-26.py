class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            word = "".join(sorted(s))
            if word not in res:
                res[word] = [s]
            else:
                res[word].append(s)
            

        return [lst for lst in res.values()]