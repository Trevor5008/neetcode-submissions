class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        rates = sorted(zip(position, speed), reverse=True)
        last, count = -1,0
        for pos, spd in rates:
            rate = (target - pos) / spd
            if not last or last < rate:
                 count += 1
                 last = rate
        return count