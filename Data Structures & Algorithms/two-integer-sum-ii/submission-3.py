"""
Given an sorted int array 'numbers'

return the indices of two number (1-indexed) such that they add up to the given
target and idx1 < idx2 

idx1 and idx2 cannot be equal (can't use the same element twice)

Ex1: numbers = [1,2,3,4], target = 3 -> [1,2]
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l, r = 0, len(numbers) - 1
        while l < r:
            currDiff = numbers[l] + numbers[r] - target
            if currDiff > 0:
                r -= 1
            elif currDiff < 0:
                l += 1
            else:
                print(f"{numbers[l]} + {numbers[r]} = {numbers[l] + numbers[r]}")
                return [l+1,r+1]

            
        return res