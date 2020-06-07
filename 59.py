class Solution:
    def generateMatrix(self, n: int) -> list:
        nums = [ i for i in range(1, n**2+1)]
        matrix = [[None for i in range(n)] for i in range(n)]# 初始化一个二维矩阵
        dx = [0, 1, 0, -1]# 定义移动方向
        dy = [1, 0, -1, 0]
        visited = set()
        x, y = 0, 0 # 移动的初始位置
        di = 0 # 用来决策移动的方向
        for i in range(n**2):
            matrix[x][y] = nums[i]
            visited.add((x,y))
            xc, yc = x + dx[di], y + dy[di]
            if 0<=xc<n and 0<=yc<n and (not (xc, yc) in visited):#当新坐标未越界且未遍历过时
                x, y = xc, yc
            else:# 否则
                di = (di+1)%4
                x, y = x + dx[di], y + dy[di]
        return matrix

res = Solution().generateMatrix(4)
print(res)
