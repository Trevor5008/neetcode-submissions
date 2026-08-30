"""
Given an array of strings (strs)
group all anagrams into sublists

Ex1: ["act", "pots", "tops", "cat", "stop", "hat"]
-> [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = {}
        for string in strs:
            word = "".join(sorted(string))
            print(word)
            if word in wordMap:
                wordMap[word].append(string)
            else:
                wordMap[word] = [string]
        return [lsts for lsts in wordMap.values()]