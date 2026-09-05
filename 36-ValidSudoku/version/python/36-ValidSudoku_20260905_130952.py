# Last updated: 05/09/2026, 13:09:52
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        seen = defaultdict(set)
4        
5        for i in range(0, 9):
6            for j in range(0, 9):
7                row_key = f"{i} row"
8                col_key = f"{j} col"
9                box_i = i // 3
10                box_j = j // 3
11                box_key = f"{box_i}, {box_j}"
12                val = board[i][j]
13
14                if val in seen[row_key] or val in seen[col_key] or val in seen[box_key]:
15                    return False
16                
17                if val != '.':
18                    seen[row_key].add(val)
19                    seen[col_key].add(val)
20                    seen[box_key].add(val)
21        
22        return True