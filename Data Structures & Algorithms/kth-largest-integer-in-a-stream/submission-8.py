import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        while len(self.nums) > k:
            self.nums.pop(0)
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        while len(self.nums) > self.k:
            self.nums.pop(0)
        print(self.nums)
        return self.nums[0]
