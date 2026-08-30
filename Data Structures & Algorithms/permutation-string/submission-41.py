class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Map, s2Map = [0]*26,[0]*26

        for i in range(len(s1)):
            s1Map[ord(s1[i]) - ord('a')] += 1
            s2Map[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Map[i] == s2Map[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            charIdx = ord(s2[l]) - ord('a')
            s2Map[charIdx] -= 1
            if s1Map[charIdx] == s2Map[charIdx]:
                matches += 1
            elif s1Map[charIdx] == s2Map[charIdx] + 1:
                matches -= 1

            l += 1
            charIdx = ord(s2[r]) - ord('a')
            s2Map[charIdx] += 1
            if s1Map[charIdx] == s2Map[charIdx]:
                matches += 1
            elif s1Map[charIdx] == s2Map[charIdx] - 1:
                matches -= 1
        return matches == 26