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
        if target == "0000":
            return 0

        visit = set(deadends)
        if "0000" in visit:
            return -1

        q = deque(["0000"])
        visit.add("0000")
        steps = 0

        while q:
            steps += 1
            for _ in range(len(q)):
                lock = q.popleft()
                for i in range(4):
                    for j in [1, -1]:
                        digit = str((int(lock[i]) + j + 10) % 10)
                        nextLock = lock[:i] + digit + lock[i+1:]
                        if nextLock in visit:
                            continue
                        if nextLock == target:
                            return steps
                        q.append(nextLock)
                        visit.add(nextLock)
        return -1

