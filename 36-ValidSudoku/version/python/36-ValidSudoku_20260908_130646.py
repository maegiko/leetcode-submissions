# Last updated: 08/09/2026, 13:06:46
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        row_seen = defaultdict(set)
4        col_seen = defaultdict(set)
5        box_seen = defaultdict(set)
6
7        for i in range(0, 9):
8            for j in range(0, 9):
9                val = board[i][j]
10                
11                if val == '.':
12                    continue
13                    
14                box_key = f"{i // 3}, {j // 3}"
15
16                if val in row_seen[i] or val in col_seen[j] or val in box_seen[box_key]:
17                    print(row_seen[i], col_seen[j], box_seen[box_key])
18                    return False
19                else:
20                    row_seen[i].add(val)
21                    col_seen[j].add(val)
22                    box_seen[box_key].add(val)
23        
24        return True