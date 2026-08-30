from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends: return -1

        visited = set(deadends)
        q = deque()
        q.append(("0000", 0))

        while q:
            curr, turns = q.popleft()

            if curr == target:
                return turns
            for i in range(4):
                for delta in [-1,1]:
                    digit = str((int(curr[i]) + delta) % 10)
                    nxt = curr[:i] + digit + curr[i+1:]
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, turns + 1))
        return -1