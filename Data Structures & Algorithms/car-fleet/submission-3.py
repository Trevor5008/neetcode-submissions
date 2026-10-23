class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = [] # arrival time of fleets
        for p, s in cars:
            time = (target - p) / s
            if stack and time <= stack[-1]:
                continue
            stack.append(time) # this car forms a new fleet
        return len(stack) 