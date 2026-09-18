# Last updated: 18/09/2026, 23:46:43
1class Solution:
2    def isValidSudoku(self, board: list[list[str]]) -> bool:
3        rowSeen = defaultdict(set)
4        colSeen = defaultdict(set)
5        boxSeen = defaultdict(set)
6
7        for i in range(len(board)):
8            for j in range(len(board[i])):
9                val = board[i][j]
10
11                if val == '.':
12                    continue
13
14                boxKey = str(i // 3) + " - " + str(j // 3)
15
16                if val in rowSeen[i] or val in colSeen[j] or val in boxSeen[boxKey]:
17                    return False
18                
19                rowSeen[i].add(val)
20                colSeen[j].add(val)
21                boxSeen[boxKey].add(val)
22        
23        return True