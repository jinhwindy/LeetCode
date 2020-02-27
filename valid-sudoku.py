class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[{} for i in range(9)]
        col=[{} for i in range(9)]
        box=[{} for i in range(9)]


        for i in range(9):
            for j in range(9):
                num=board[i][j]
                if num!='.':
                    number=int(num)
                    boxindex=(i//3)*3+j//3
                    row[i][number]=row[i].get(number,0)+1
                    col[j][number]=col[j].get(number,0)+1
                    box[boxindex][number]=box[boxindex].get(number,0)+1

                    if row[i][number]>1 or col[j][number]>1 or box[boxindex][number]>1:
                        return False
        return True
