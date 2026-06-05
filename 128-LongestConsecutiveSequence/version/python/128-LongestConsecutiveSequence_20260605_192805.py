# Last updated: 05/06/2026, 19:28:05
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        numbers = set(nums)
4        
5        maxLen = 0
6        for num in numbers:
7            if (num - 1) not in numbers:
8                count = 1
9                while (num + 1 in numbers):
10                    count += 1
11                    num += 1
12                
13                maxLen = max(count, maxLen)
14        
15        return maxLen
16
17            
18
19
20
21