class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'{':'}','(':')','[':']'}
        stack = []

        for char in s:
            if char in pairs.keys():
                stack.append(char)
            elif len(stack) and char == pairs[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0