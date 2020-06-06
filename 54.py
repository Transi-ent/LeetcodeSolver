class Solution:
    def spiralOrder(self, matrix: list) -> list:
        res = []
        while matrix:
            # 添加第一行
            res += matrix.pop(0)
            # 添加最后一列
            if matrix and matrix[0]:
                for lyst in matrix:
                    res.append(lyst.pop())
            else:
                break
            # 添加最后一行
            if matrix and matrix[0]:
                last = matrix.pop()
                res+=last[::-1]
            else:
                break
            # 添加第一列
            if matrix and matrix[0]:
                for lyst in matrix[::-1]:
                    res.append(lyst.pop(0))
            else:
                break
        return res

res = Solution().spiralOrder([
    [1,2,3,4],
    [5,6,7,8],
    [9, 10,11,12]
])
print(res)
