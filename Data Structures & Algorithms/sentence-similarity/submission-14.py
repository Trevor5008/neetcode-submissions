class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False
        
        pairs = set()
        for p in similarPairs:
            pairs.add((p[0], p[1]))
            pairs.add((p[1], p[0]))
            
        for w1, w2 in zip(sentence1, sentence2):
            if w1 != w2 and (w1, w2) not in pairs:
                return False
                    
        return True