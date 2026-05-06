# Last updated: 06/05/2026, 19:09:23
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
13
14        for num in nums1:
15            if num not in set2 and num not in res[0]:
16                res[0].append(num)
17        
18        for num in nums2:
19            if num not in set1 and num not in res[1]:
20                res[1].append(num)
21        
22        return res