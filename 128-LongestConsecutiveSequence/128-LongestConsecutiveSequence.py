# Last updated: 18/08/2026, 14:57:23
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        
        maxLen = 0
        for num in numbers:
            if (num - 1) not in numbers:
                count = 1
                while (num + 1 in numbers):
                    count += 1
                    num += 1
                
                maxLen = max(count, maxLen)
        
        return maxLen

            



