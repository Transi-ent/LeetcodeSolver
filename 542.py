class Solution:
    """
    广度优先遍历，往 4 个方向进行搜索，如果所搜索到的点的取值小于原来的值，则放入队列进行更新，
    ...否则不放入队列。
    """
    def updateMatrix(self, matrix: list) -> list:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        m, n = len(matrix), len(matrix[0])
        queue = []
        brek = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append([i, j])
                    brek = True
                    break
            if brek:
                break

        visited = [[0]*n for _ in range(m)]

        while queue:
            p = queue.pop(0)
            val = matrix[p[0]][p[1]]
            #visited[p[0]][p[1]] = 1
            for i in range(4):
                x = p[0] + dx[i]
                y = p[1] + dy[i]
                if x<0 or x>=m or y<0 or y>=n:
                    continue
                #print("x:{}, y:{}".format(x, y))
                if visited[x][y]==0:
                    if matrix[x][y]!=0:
                        matrix[x][y] = val+1
                    visited[x][y]=1
                    queue.append([x, y])

                if visited[x][y] and matrix[x][y]>val+1:
                    matrix[x][y] = val+1
                    queue.append([x, y])

        print(matrix)
        return matrix

Solution().updateMatrix(
    [
        [0,0,0],
        [0,1,0],
        [1,1,1]
    ]
)

