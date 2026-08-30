from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends: return -1

        visited = set(deadends)
        q = deque()
        q.append(("0000", 0))

        while q:
            combo, turns = q.popleft()

            if combo == target:
                return turns

            for i in range(4):
                for delta in [-1,1]:
                    digit = str((int(combo[i]) + delta) % 10)
                    nxt = combo[:i] + digit + combo[i+1:]
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, turns + 1))
        return -1
