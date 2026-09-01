class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            sort_w = "".join(sorted(word))
            if sort_w in groups:
                groups[sort_w].append(word)
            else:
                groups[sort_w] = [word]
        return list(groups.values())