class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}
        for str in strs:
            str_key = [0]*26
            for ch in str:
                str_key[ord(ch)-97] += 1
            key = tuple(str_key)
            str_map.setdefault(key, []).append(str)
        return list(str_map.values())