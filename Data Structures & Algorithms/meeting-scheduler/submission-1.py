class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # [start, end], duration: time (int)
        if not slots1 or not slots2: return []
        slots1.sort()
        slots2.sort()
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            slot1, slot2 = slots1[i], slots2[j]
            start = max(slot1[0], slot2[0])
            end = min(slot1[1], slot2[1])
            if start + duration <= end:
                return [start, start + duration]
            if slot1[1] < slot2[1]:
                i += 1
            else:
                j += 1
        return []