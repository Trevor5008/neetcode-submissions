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
        if "0000" in deadends:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        q = deque([("0000", 0)])
        visit = set(deadends)

        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append((child, turns + 1))
        return -1


            




