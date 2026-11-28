class Solution:
    def reorganizeString(self, s: str) -> str:
        charCt = Counter(s)
        res, maxHeap = "", []
        for char, freq in charCt.items():
            if freq > (len(s) + 1) // 2: return res
            heapq.heappush(maxHeap, (-freq, char))
        
        prev = None
        while maxHeap or prev:
            if not maxHeap and prev:
                return ""
            freq, char = heapq.heappop(maxHeap)
            res += char
            freq += 1
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
                
            if freq < 0:
                prev = (freq, char)
            
        return res