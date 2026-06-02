# Last updated: 02/06/2026, 16:54:24
1class Solution:
2    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
3        land_start = self.calculateMinimumTime(landStartTime, landDuration, waterStartTime, waterDuration)
4        water_start = self.calculateMinimumTime(waterStartTime, waterDuration, landStartTime, landDuration)
5
6        return min(land_start, water_start)
7    
8    def calculateMinimumTime(self, firstRide: List[int], firstDuration: List[int], secondRide: List[int], secondDuration: List[int]) -> int:
9        firstRideMin = float("inf")
10
11        for i in range(len(firstRide)):
12            firstRideMin = min(firstRideMin, firstRide[i] + firstDuration[i])
13
14        totalMin = float("inf")
15        for j in range(len(secondRide)):
16            totalTime = firstRideMin
17
18            if secondRide[j] <= firstRideMin:
19                totalTime += secondDuration[j]
20            else:
21                waitTime = secondRide[j] - firstRideMin
22                totalTime += waitTime + secondDuration[j]
23            
24            totalMin = min(totalMin, totalTime)
25        
26        return totalMin