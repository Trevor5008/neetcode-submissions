class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        numSubs = 0
        currSum = 0
        # Use a hash map to store frequency of prefix sums
        # Initialize with {0: 1} to handle subarrays starting from index 0
        counts = {0: 1}
        
        for num in nums:
            currSum += num
            # If (currSum - k) exists in counts, it means a subarray sum equals k
            if currSum - k in counts:
                numSubs += counts[currSum - k]
            
            # Update the frequency of the current prefix sum
            counts[currSum] = counts.get(currSum, 0) + 1
            
        return numSubs