class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False

        for words in zip(sentence1, sentence2):
            w1, w2 = words
            if [w1, w2] not in similarPairs and [w2, w1] not in similarPairs and w1 != w2:
                return False
        return True