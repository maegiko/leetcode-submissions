# Last updated: 18/08/2026, 14:56:25
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for x in range(len(nums) + 1)]

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for key, value in freq.items():
            bucket[value].append(key)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for j in range(len(bucket[i])):
                res.append(bucket[i][j])

                if len(res) == k: return res
