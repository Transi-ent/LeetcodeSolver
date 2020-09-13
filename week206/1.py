class Solution:
    """
    先分别对每一行进行计算，用dict记录每一行和为1的行号和列号（Key:row, value:col）
    然后以列进行计算，和为1的列将RES+1
    """
    def numSpecial(self, mat: list) -> int:
        if len(mat)==0 or len(mat[0])==0:
            return 0
        m, n, res = len(mat), len(mat[0]), 0

        pos = {}
        for i, row in enumerate(mat):
            if sum(row)==1:
                col = row.index(1)
                pos[i] = col

        for row, col in pos.items():
            tmp = 0
            for j in range(m):
                tmp += mat[j][col]
                if tmp>1:
                    break

            if tmp==1:
                res += 1
        return res


mat = [[1,0,0],
            [0,1,0],
            [0,0,1]]
res = Solution().numSpecial(mat)

print(res)
