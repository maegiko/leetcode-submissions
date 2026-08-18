# Last updated: 18/08/2026, 14:58:09
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, max_reach, current_end = 0, 0, 0

        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = max_reach
        
        return jumps

