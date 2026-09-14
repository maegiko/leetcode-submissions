# Last updated: 14/09/2026, 22:49:54
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        res = max(piles)
4        l, r = 1, res
5
6        while l <= r:
7            k = (l + r) // 2
8
9            hte = 0
10            for p in piles:
11                hte += math.ceil(p / k)
12            
13            if hte > h:
14                l = k + 1
15            else:
16                r = k - 1
17                res = min(k, res)
18        
19        return res
20        