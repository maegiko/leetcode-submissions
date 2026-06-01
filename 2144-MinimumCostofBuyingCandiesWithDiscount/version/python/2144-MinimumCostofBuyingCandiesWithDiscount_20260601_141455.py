# Last updated: 01/06/2026, 14:14:55
1class Solution:
2    def minimumCost(self, cost: List[int]) -> int:
3        cost.sort(reverse = True)
4        total = 0
5
6        for i in range(len(cost)):
7            if (i % 3 != 2):
8                total += cost[i]
9        
10        return total
11
12