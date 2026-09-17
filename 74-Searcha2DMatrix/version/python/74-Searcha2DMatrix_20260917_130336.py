# Last updated: 17/09/2026, 13:03:36
1class Solution:
2    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
3        mL, mR = 0, len(matrix) - 1
4
5        while mL <= mR:
6            mid = (mL + mR) // 2
7
8            if matrix[mid][0] < target:
9                mL = mid + 1
10            elif matrix[mid][0] > target:
11                mR = mid - 1
12            else:
13                return True
14        
15
16        if mR < 0:
17            return False
18
19        nL, nR = 0, len(matrix[mR]) - 1
20
21        while nL <= nR:
22            mid = (nL + nR) // 2
23
24            if matrix[mR][mid] < target:
25                nL = mid + 1
26            elif matrix[mR][mid] > target:
27                nR = mid - 1
28            else:
29                return True
30        
31        return False
32