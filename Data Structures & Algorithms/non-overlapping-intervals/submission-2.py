"""
Given an array of intervals where intervals[i] = [start_i, end_i]
return the minimum number of intervals you need to remove to make
the rest of the intervals non-overlapping
E.C: [1,2], [2,3] are non-overlapping

Ex1: intervals = [[1,2],[2,4],[1,4]] -> 1 ([1,4])
Ex2: intervals = [[1,2],[2,4]] -> 0
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        selected = []
        # Sort activities in ascending order based on completion time
        intervals.sort(key=lambda x: x[1])
        selected.append(intervals[0])
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] >= selected[-1][1]:
                selected.append(curr)
        return len(intervals) - len(selected)