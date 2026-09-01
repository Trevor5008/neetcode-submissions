class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            sortw = "".join(sorted(word))
            if sortw in groups:
                groups[sortw].append(word)
            else:
                groups[sortw] = [word]
        return [lst for lst in groups.values()]