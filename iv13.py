class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        res = 0
        grid = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                j_sum = self.f(j)
                i_sum = self.f(i)
                if j_sum+i_sum<=k:
                    res += 1
                    grid[i][j]=1
                else:
                    print("Sum of all digits:{},i={},j={}".format(i_sum+j_sum,i,j))
                    break
            if self.f(i)>k:
                break
        for i, l  in enumerate(grid):

            print(i,": ",l)
        return res
    def f(self, n):
        """
        :param n: a number >=0
        :return: the sum of all digits
        """
        res = 0
        while n>=10:
            n, rem = divmod(n, 10)
            res += rem
        return n+res

class Solution2:
    """
    BFS
    只需要从（0, 0）开始，分别向右和向下搜索即可，并记录所遍历过的点
    """
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = [[0]*n for _ in range(m)] # 0: 未遍历，1: 遍历过
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        res = 0
        queue = [[0, 0]]
        while queue:
            p = queue.pop()
            if self.f(p[0])+self.f(p[1])<=k and visited[p[0]][p[1]]==0:
                visited[p[0]][p[1]] = 1
                res += 1
            for i in range(4):
                x = p[0] + dx[i]
                y = p[1] + dy[i]
                if x<0 or y<0 or x>=m or y>=n or visited[x][y]==1:
                    # 若越界或者遍历过，直接看下一个点
                    continue
                if visited[p[0]][p[1]]:
                    queue.append([x, y])
        s1 = 0
        for i, l in enumerate(visited):
            s1 += sum(l)
            print("{}: {}".format(i, l))

        print(s1)
        return res

    def f(self, n):
        res = 0
        while n>=10:
            n, rem = divmod(n, 10)
            res += rem
        return n+res



















res = Solution2().movingCount(38, 15, 9)
print(res)
