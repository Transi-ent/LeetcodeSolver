class Solution:
    """
    将表面积的计算分为2个部分，一个是边界区域的外部部分，
    一个是方块相邻接的内部部分
    """
    def surfaceArea(self, grid: list) -> int:
        if len(grid)==0 or grid[0]==0:
            return 0
        m, n = len(grid), len(grid[0])
        if m==1 and n==1:
            return grid[0][0]*4 + 2
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res += 2  # up, down
                if i==0 or j==0 or i==m-1 or j==n-1:
                    # 若在第一行/列 或 最后一行/列
                    res += grid[i][j] # back,front,left,right
                if i==0:
                    if j!=0:
                        res += abs( grid[i][j]-grid[i][j-1] )
                else:
                    if j!=0:
                        res += abs( grid[i][j]-grid[i][j-1] )
                        res += abs( grid[i][j]-grid[i-1][j] )
                    else:
                        res += abs( grid[i][j]-grid[i-1][j] )
        # 补充位于角落的立方体面积
        res += grid[0][0]
        res += grid[0][-1]
        res += grid[-1][0]
        res += grid[-1][-1]
        return res



