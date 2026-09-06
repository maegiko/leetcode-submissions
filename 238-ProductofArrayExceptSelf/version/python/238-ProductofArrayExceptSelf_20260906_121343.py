# Last updated: 06/09/2026, 12:13:43
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        product = 1
4        pre = [(pre_product := product, product := product * num)[0] for num in nums]
5
6        product = 1
7        post = [None] * len(nums)
8        for i in range(len(nums) - 1, -1, -1):
9            post[i] = product
10            product *= nums[i]
11
12        return ([(pre[i] * post[i]) for i in range(len(nums))])