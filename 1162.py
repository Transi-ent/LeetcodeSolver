class Solution:
    """
    使用广度优先搜索，每一块陆地都是一个源
    从陆地出发，一开始先把陆地入列，依次访问陆地可以访问的临近区域，
    ...并记录所访问过的
    """
    def maxDistance(self, grid: list) -> int:
        n = len(grid)
        dx = [0,0,1,-1]
        dy = [-1,1,0,0]
        queue = list()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append([i, j])
        if len(queue)==n**2:
            return -1
        point = None
        while queue:
            point = queue.pop(0)
            for i in range(4):
                xi = point[0] + dx[i]
                yi = point[1] + dy[i]

                if xi<0 or xi>=n or yi<0 or yi>=n or grid[xi][yi]!=0:
                    continue
                queue.append([xi, yi])
                grid[xi][yi] = grid[point[0]][point[1]] + 1

        if point is None:
            return -1
        print(grid)
        return grid[point[0]][point[1]] - 1

Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]])
