class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        return [x[0] for x in counts][:k]