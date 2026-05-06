# Last updated: 06/05/2026, 19:15:19
1class Solution:
2    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
3        set1 = set()
4        set2 = set()
5
6        for num in nums1:
7            set1.add(num)
8        
9        for num in nums2:
10            set2.add(num)
11
12        res = [[] for x in range(0, 2)]
13        res[0] = list(set1 - set2)
14        res[1] = list(set2 - set1)
15        return res