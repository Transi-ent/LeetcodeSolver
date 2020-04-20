class Solution:
    """
    广度优先遍历
    使用 grid 双层数组本身去记录是否遍历过，若大于2，表示遍历过
    """
    def numIslands(self, grid: list) -> int:
        # for s in grid:
        #
        m = len(grid)
        if m==0:
            return 0
        n = len(grid[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        res = 0
        for i in range(m):
            for j in range(n):
                print("i: {}, j: {}".format(i, j))
                if grid[i][j]=='1':
                    print("====> i: {}, j: {}".format(i, j))
                    queue = [(i, j)]
                    grid[i][j] = '2'
                    res += 1
                    while queue:
                        p = queue.pop(0)
                        for k in range(4):
                            x = p[0] + dx[k]
                            y = p[1] + dy[k]
                            if x<0 or x>=m or y<0 or y>=n or \
                                int(grid[x][y])>1 or grid[x][y]=='0':
                                continue
                            grid[x][y] = str( int(grid[x][y]) + 1)
                            queue.append((x, y))
        print(res)
        return res

grid = [['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1']
    ]

Solution().numIslands(grid)
