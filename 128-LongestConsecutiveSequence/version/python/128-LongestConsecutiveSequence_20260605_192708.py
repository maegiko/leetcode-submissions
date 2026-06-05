# Last updated: 05/06/2026, 19:27:08
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        numbers = set()
4
5        for num in nums:
6            numbers.add(num)
7        
8        maxLen = 0
9        for num in numbers:
10            if (num - 1) not in numbers:
11                count = 1
12                while (num + 1 in numbers):
13                    count += 1
14                    num += 1
15                
16                maxLen = max(count, maxLen)
17        
18        return maxLen
19
20            
21
22
23
24