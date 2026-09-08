# Last updated: 08/09/2026, 14:13:45
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        pos_speed = []
4        for i in range(len(position)):
5            pos_speed.append((position[i], speed[i]))
6        
7        pos_speed.sort(reverse=True)
8
9        fleets = len(pos_speed)
10        max_tta = 0 # time to arrive
11
12        for c in pos_speed:
13            tta = (target - c[0]) / c[1] # calculate time to arrive
14
15            if tta > max_tta:
16                max_tta = tta
17            elif tta <= max_tta:
18                fleets -= 1
19
20        return fleets
21