# Last updated: 06/05/2026, 16:25:37
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        freq = {}
4        bucket = [[] for x in range(len(nums) + 1)]
5
6        for num in nums:
7            freq[num] = 1 + freq.get(num, 0)
8        
9        for key, value in freq.items():
10            bucket[value].append(key)
11        
12        res = []
13        for i in range(len(bucket) - 1, 0, -1):
14            for j in range(len(bucket[i])):
15                res.append(bucket[i][j])
16
17                if len(res) == k: return res
18