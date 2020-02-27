class Solution:        
    def dfs(self,board,row,col,box,i,j)->bool:
    # 确定一个从给定i，j值开始的可以填写的空格
        while board[i][j]!='.':
            j+=1
            if j>=9:
                i+=1
                j=0
            if i>=9:
                return True
        
        for num in range(9):
            boxindex=(i//3)*3+j//3
            if row[i][num]==0 and col[j][num]==0 and box[boxindex][num]==0:
                row[i][num]=1
                col[j][num]=1
                box[boxindex][num]=1
                board[i][j]=str(num+1)
                # /////////////////////////////////////////
                if self.dfs(board,row,col,box,i,j):
                    return True
                else :
                    row[i][num]=0
                    col[j][num]=0
                    box[boxindex][num]=0
                    board[i][j]='.'


    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
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
        thing=self.dfs(board,row,col,box,0,0)
