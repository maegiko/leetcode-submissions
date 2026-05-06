# Last updated: 06/05/2026, 18:35:19
1class Solution:
2    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
3        if n == 0: return True
4
5        if len(flowerbed) == 1:
6            if flowerbed[0] == 0:
7                return True
8            else:
9                return False
10
11        count = 0
12        for i in range(len(flowerbed)):
13            if (i == 0):
14                if flowerbed[i] == 0 and flowerbed[i + 1] == 0: 
15                    count += 1
16                    flowerbed[i] = 1
17            elif (i == len(flowerbed) - 1):
18                if flowerbed[i] == 0 and flowerbed[i - 1] == 0: 
19                    count += 1
20                    flowerbed[i] = 1
21            else:
22                if (flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0):
23                    count+=1
24                    flowerbed[i] = 1
25
26            if (count == n): return True
27        
28        return False