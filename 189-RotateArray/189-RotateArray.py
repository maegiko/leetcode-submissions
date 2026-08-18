# Last updated: 18/08/2026, 14:57:08
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        shifts = []
        num_shifts = k - 1

        for i in range(len(nums)):
            if (i == (len(nums) - 1) - num_shifts):
                shifts.append(nums[i])
                num_shifts -= 1
                nums[i] = None

        right = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] is not None:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
        
        for i in range(0, k):
            nums[i] = shifts[i]


    
        


        