class Solution:
    """
    BFS未通过：当搜索到一定深度时，字符串不能继续匹配了，需要返回到上一深度继续匹配，为进行此处理
    """
    def exist(self, board: list, word: str) -> bool:
        if len(board)==0 or len(board[0])==0:
            return False

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        ptr = 0
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    print("NEW Start")
                    visited = [[0 for _ in range(n)] for _ in range(m)]  # 0——未遍历，^0——已遍历
                    q = [(i, j)]
                    while q:
                        xi, yi = q.pop(0)
                        print("xi={}, yi={}".format(xi, yi))
                        if board[xi][yi]==word[ptr]:
                            q = [] # 当前字符已经校对完毕，需要将队列置空，否则存放当前位置和下一个字符位置的将影响判断
                            visited[xi][yi] = 1
                            ptr += 1
                            if ptr>=len(word):
                                return True
                            for k in range(4):
                                x = xi + dx[k]
                                y = yi + dy[k]
                                if 0 <= x < m and 0 <= y < n and visited[x][y] == 0:
                                    q.append((x, y))
                    ptr = 0

        return False

class Solution2:
    """
    DFS
    """
    def exist(self, board: list, word: str) -> bool:
        def dfs(i: int, j: int, k: int) ->bool:
            if not 0<=i<m or not 0<=j<n or board[i][j]!=word[k]:
                return False
            if k==len(word)-1:
                return True
            tmp, board[i][j] = board[i][j], ''# 为了避免重复的使用同一个字符，将当前判断过的位置制成一个不可能的字符
            res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j-1, k+1) or dfs(i, j+1, k+1)
            board[i][j] = tmp # 回溯法：当某一个递归分支没有成功过的递归到底时，需要还原原位置字符
            return res

        if len(board)==0 or len(board[0])==0:
            return False

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False




board = [["C","A","A"],["A","A","A"],["B","C","D"]]

word = "AAB"
print(Solution().exist(board, word))

