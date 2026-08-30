class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        stack = stones
        while len(stack) > 1:
            curr = stack.pop(-1)
            if curr == stack[-1]:
                stack.pop()
            elif curr > stack[-1]:
                stack.append(curr - stack.pop(-1))
            elif curr < stones[-1]:
                stack.append(stack.pop(-1) - curr)
            stack.sort()
            print(stack)
        return 0 if not stack else stack[0]