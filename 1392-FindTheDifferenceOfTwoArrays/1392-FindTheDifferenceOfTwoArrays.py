# Last updated: 18/08/2026, 14:55:57
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set()
        set2 = set()

        for num in nums1:
            set1.add(num)
        
        for num in nums2:
            set2.add(num)

        res = [[] for x in range(0, 2)]
        res[0] = list(set1 - set2)
        res[1] = list(set2 - set1)
        return res