class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        brackets = {'(':')','{':'}','[':']'}
        for char in s:
            if char in brackets:
                queue.append(char)
            elif queue and char == brackets[queue[-1]]:
                queue.pop()
            else: 
                return False

        return len(queue) == 0