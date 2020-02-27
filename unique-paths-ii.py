class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        if m==0:
            return 0
        n=len(obstacleGrid[0])
        if n==0:
            return 0
        if obstacleGrid[0][0]==1:
            return 0

        obstacleGrid[0][0]=1
        for i in range(1,n):
            if obstacleGrid[0][i-1]==1 and obstacleGrid[0][i]==0:
                obstacleGrid[0][i]=1
            else:
                obstacleGrid[0][i]=0
        for i in range(1,m):
            if obstacleGrid[i-1][0]==1 and obstacleGrid[i][0]==0:
                obstacleGrid[i][0]=1
            else:
                obstacleGrid[i][0]=0
        print(obstacleGrid)
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]:
                    obstacleGrid[i][j]=0
                else:
                    obstacleGrid[i][j]=obstacleGrid[i][j-1]+obstacleGrid[i-1][j]
        return obstacleGrid[m-1][n-1]
