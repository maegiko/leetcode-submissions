# Last updated: 13/05/2026, 00:19:35
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        res = []
4        left = 0
5        right = len(numbers) - 1
6
7        while (left < right):
8            if numbers[left] + numbers[right] > target:
9                right -= 1
10            elif numbers[left] + numbers[right] < target:
11                left += 1
12            else:
13                res.append(left + 1)
14                res.append(right + 1)
15                break
16        
17        return res