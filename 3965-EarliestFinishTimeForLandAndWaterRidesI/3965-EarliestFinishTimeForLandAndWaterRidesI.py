# Last updated: 18/08/2026, 14:55:30
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        land_start = self.calculateMinimumTime(landStartTime, landDuration, waterStartTime, waterDuration)
        water_start = self.calculateMinimumTime(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(land_start, water_start)
    
    def calculateMinimumTime(self, firstRide: List[int], firstDuration: List[int], secondRide: List[int], secondDuration: List[int]) -> int:
        firstRideMin = float("inf")

        for i in range(len(firstRide)):
            firstRideMin = min(firstRideMin, firstRide[i] + firstDuration[i])

        totalMin = float("inf")
        for j in range(len(secondRide)):
            totalTime = firstRideMin

            if secondRide[j] <= firstRideMin:
                totalTime += secondDuration[j]
            else:
                waitTime = secondRide[j] - firstRideMin
                totalTime += waitTime + secondDuration[j]
            
            totalMin = min(totalMin, totalTime)
        
        return totalMin