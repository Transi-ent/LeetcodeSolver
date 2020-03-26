class Solution:
    """
    先进行遍历，求出白车所在的位置（Row，Col），
    再次进行遍历，查询所在的行和列可以捕获的卒
    """
    def numRookCaptures(self, board: list) -> int:
        r, c = None, None
        flag = False
        for i in range(8):
            for j in range(8):
                if board[i][j]=="R":
                    r, c = i, j
                    flag = True
                    break
            if flag:
                break
        up, down, left, right = 0,0,0,0
        hasBishop = False
        for i in range(8):
            for j in range(8):
                if j==c and i<r:
                    if board[i][j]=="B":
                        up = 0
                    elif board[i][j]=='p':
                        up = 1
                elif i==r:
                    if j<c:
                        if board[i][j]=='p':
                            left = 1
                        elif board[i][j]=="B":
                            left = 0
                    elif j>c:
                        if board[i][j]=="B":
                            break
                        elif board[i][j]=='p':
                            right = 1
                elif i>r and j==c:
                    if board[i][j]=='B':
                        hasBishop = True
                        break
                    elif board[i][j]=='p':
                        down = 1
            if hasBishop:
                break
        return up+down+left+right
