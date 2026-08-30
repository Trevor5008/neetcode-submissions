"""
Given an array 'arr', replace every element in the array w/ the greatest element among
the elements to its right, and replace the last element w/ -1

Ex1. arr = [2,4, 5, 3, 1, 2] -> [5,5,3,2,2,-1]
Ex2. arr = [3,3] -> [3, -1]
"""
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            if arr[i]:
                arr[i] = max(arr[i+1:])
        arr[len(arr)-1] = -1
        return arr