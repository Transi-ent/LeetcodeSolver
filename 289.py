class Solution:
    """
    为了方便统一处理，将 Board 数组周边填充上一圈0，并不会改变原结果
    """
    def gameOfLife(self, board: list) -> None:
        import copy
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        boardBefore = copy.deepcopy(board)
        boardBefore.insert(0, [0]*n)
        boardBefore.append([0]*n)
        boardBefore = [[0]+lyst+[0] for lyst in boardBefore]


        for i in range(1, len(boardBefore)-1):
            for j in range(1, len(boardBefore[0])-1):
                tmpSum = boardBefore[i-1][j-1]+boardBefore[i-1][j]+\
                    boardBefore[i-1][j+1]+boardBefore[i][j-1]+boardBefore[i][j+1]\
                + boardBefore[i+1][j-1]+boardBefore[i+1][j] + boardBefore[i+1][j+1]
                if tmpSum<2:
                    board[i-1][j-1] = 0
                elif tmpSum==2 or tmpSum==3:
                    if boardBefore[i][j]==0 and tmpSum==3:
                        board[i - 1][j - 1] = 1
                elif tmpSum>3 and boardBefore[i][j]==1:
                    board[i - 1][j - 1] = 0
                # for i in range(len(board)):
                print("i: {}, j: {}".format(i, j))

Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])

