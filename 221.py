class Solution:
    """
    暴力解，搜索，4 层循环
    首先在矩阵内检测 1 的存在，检测到之后接着去检查相邻一圈（该正方形的下一行和下来一列）是否为1，
    """
    def maximalSquare(self, matrix: list) -> int:
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='1':
                    print("i={}, j={}".format(i, j))
                    longth = 1
                    res = max(res, longth**2)
                    colFin, rowFin = False, False
                    while True:
                        print("longth={}".format(longth))
                        for k in range(i, i+longth+1):
                            if k>=len(matrix) or j+longth>=len(matrix[0]):
                                break
                            if matrix[k][j+longth]=='0':
                                break
                            if k==i+longth:
                                colFin = True
                        for k in range(j, j+longth):
                            if k>=len(matrix[0]) or i+longth>=len(matrix):
                                break
                            if matrix[i+longth][k]=='0':
                                break
                            if k==j+longth-1:
                                rowFin = True
                        if colFin and rowFin:
                            longth += 1
                            res = max(res, longth ** 2)
                            colFin, rowFin = False, False
                        else:
                            break
        print(res)
        return res

class Solution2:
    """
    动态规划
    状态转移方程：dp[i][j]=min( dp[i-1][j], dp[i][j-1], dp[i-1][j-1] ) + 1
    """
    def maximalSquare(self, matrix: list) -> int:

        if len(matrix)<1 or len(matrix[0])<1:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0]*(cols+1) for i in range(rows+1)]
        maxLen = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]=='1':
                    dp[i+1][j+1]=min( dp[i][j], dp[i+1][j], dp[i][j+1] ) + 1
                    maxLen = max(maxLen, dp[i+1][j+1])
        print(maxLen**2)
        return maxLen**2

matrix = [
    ['1','0','1','0','0'],
    ['1','0','1','1','1'],
    ['1','1','1','1','1'],
    ['1','0','1','1','1']
]
Solution2().maximalSquare(matrix)
