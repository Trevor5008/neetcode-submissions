class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        groups = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in groups:
            time = (target - pos) / spd
            if not stack or stack[-1] < time:
                stack.append(time)
        print(stack)
        return len(stack)