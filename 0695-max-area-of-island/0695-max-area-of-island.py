class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Max = 0
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    Area = self.getArea(grid , i , j , m , n)
                    Max = max(Max,Area)
        return Max
    def getArea(self, grid: list[list[int]], i: int, j: int, m: int, n: int) -> int:
        if (i<0 or j<0 or i>=m or j >=n or grid[i][j]==0):
            return 0
        grid[i][j]=0
        left = self.getArea(grid,i,j-1,m,n)
        right = self.getArea(grid,i,j+1,m,n)
        up = self.getArea(grid,i-1,j,m,n)
        down = self.getArea(grid,i+1,j,m,n)
        return left+right+up+down+1