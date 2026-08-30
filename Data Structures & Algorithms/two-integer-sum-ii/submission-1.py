class Solution:
    # O(n) time, O(1) space
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            diff = target - numbers[left]
            if diff in numbers:
                return [left+1, numbers.index(diff)+1]
            left += 1
        return []


            