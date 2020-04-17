class Solution:
    def exist(self, board: list, word: str) -> bool:

        def wordSearch(wi: int, s:set, i: int, j: int) -> bool:
            if wi>len(word)-1:
                return True
            ret = False
            for k in range(4):
                xi = i + dx[k]
                yi = j + dy[k]
                if xi < 0 or xi >= m or yi < 0 or yi >= n:
                    continue
                if word[wi]==board[xi][yi] and not (xi, yi) in s:
                    print("Ch: {},wi: {} (i, j): {} {}".format(word[wi], wi, xi, yi))
                    copyOfS = s.copy()
                    copyOfS.add((xi, yi))
                    ret = ret or wordSearch(wi+1, copyOfS, xi, yi)

            return ret

        m, n = len(board), len(board[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(m):
            for j in range(n):

                if board[i][j]==word[0]:
                    print("Ch: {}, wi: {}, (i, j): {} {}".format(word[0],0, i, j))
                    # 开启单词搜索
                    ret = wordSearch( 1,  {(i,j)}, i, j)

                    if ret:
                        return True
        return False

board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
res = Solution().exist([["C","A","A"],
                        ["A","A","A"],
                        ["B","C","D"]],"AAB")
print(res)
