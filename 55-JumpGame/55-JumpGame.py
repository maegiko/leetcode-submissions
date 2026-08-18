# Last updated: 18/08/2026, 14:58:05
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0

        for i in range(len(nums)):
            if reach < 0: return False

            if nums[i] > reach:
                reach = nums[i]
            
            reach -= 1
        
        return True