# Last updated: 05/09/2026, 13:13:11
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        seen = defaultdict(set)
4        
5        for i in range(0, 9):
6            for j in range(0, 9):
7                val = board[i][j]
8                
9                if val == '.':
10                    continue
11                
12                row_key = f"{i} row"
13                col_key = f"{j} col"
14                box_i = i // 3
15                box_j = j // 3
16                box_key = f"{box_i}, {box_j}"
17
18                if val in seen[row_key] or val in seen[col_key] or val in seen[box_key]:
19                    return False
20                
21                seen[row_key].add(val)
22                seen[col_key].add(val)
23                seen[box_key].add(val)
24        
25        return True