from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets, last_time = 0, 0.0

        for pos, spd in cars:
            arrival_time = (target - pos) / spd        
            if arrival_time > last_time:
                fleets += 1
                last_time = arrival_time
        return fleets