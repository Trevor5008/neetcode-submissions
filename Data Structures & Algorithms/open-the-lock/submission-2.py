"""
You have a lock w/ 4 circular wheels
Each wheel has 10 slots: '0', '1'...
The wheels can rotate freely and wrap around
Ex. '9' -> '0'
The lock initially starts at '0000'

Given a list of 'deadends' where the if the 
lock displays any of these codes, the wheels
will stop turning (unable to open)

Given a target, return the minimum total
number of turns required to open the lock
or -1 if it's impossible

Ex1: Input: deadends = ["1111","0120","2020","3333"], target = "5555"

Output: 20
"""
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        if "0000" in deadends_set: return -1
        
        queue = deque([("0000", 0)])
        visited = {"0000"}
        
        while queue:
            curr, turns = queue.popleft()
            if curr == target:
                return turns
            for i in range(4):
                digit = int(curr[i])
                for move in [-1, 1]:
                    next_digit = (digit + move) % 10
                    next_state = curr[:i] + str(next_digit) + curr[i+1:]
                    
                    if next_state not in deadends_set and next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, turns + 1))
        return -1
