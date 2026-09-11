# Last updated: 11/09/2026, 12:19:21
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        pos_speed = [(position[i], speed[i]) for i in range(0, len(position))]
4
5        pos_speed.sort(reverse=True)
6
7        max_tta = 0
8        fleets = len(position)
9        for pos, speed in pos_speed:
10            tta = (target - pos) / speed
11
12            if tta > max_tta:
13                max_tta = tta
14            else:
15                fleets -= 1
16        
17        return fleets
18