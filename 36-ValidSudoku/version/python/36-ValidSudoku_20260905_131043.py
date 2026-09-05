# Last updated: 05/09/2026, 13:10:43
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row =[set() for i in range(9)]
        col =[set() for i in range(9)]
        box =[set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                cell=board[i][j]
                if cell=='.':
                    continue
                box_index= (i//3)*3+(j//3)
                if cell in row[i]:
                    return False
                else:
                    row[i].add(cell)
                if cell in col[j]:
                    return False
                else:
                    col[j].add(cell)
                if cell in box[box_index]:
                    return False
                else:
                    box[box_index].add(cell)
        return True