class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        stack = []
        charMap = {']': '[', '}': '{', ')': '('}
        for char in s:
            if char in charMap.values():
                stack.append(char)
            else:
                if not stack or stack.pop() != charMap[char]:
                    return False
        return len(stack) == 0