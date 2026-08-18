# Last updated: 18/08/2026, 14:57:55
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

            if freq[nums[i]] <= 2:
                nums[k] = nums[i]
                k += 1
        
        return k