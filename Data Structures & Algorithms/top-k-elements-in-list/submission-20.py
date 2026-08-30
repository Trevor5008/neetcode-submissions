from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        heap = list(freqMap.items())
        heap.sort(key=itemgetter(1), reverse=True)
        res = []
        for i in range(k):
            res.append(heap[i][0])  
        return res