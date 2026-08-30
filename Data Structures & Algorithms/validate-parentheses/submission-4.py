class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charMap = {']': '[', '}': '{', ')': '('}
        for char in s:
            if char in charMap.values():
                stack.append(char)
            else:
                if not stack or stack.pop() != charMap[char]:
                    return False
        return len(stack) == 0