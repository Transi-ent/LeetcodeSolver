class Solution:
    def spiralOrder(self, matrix: list) -> list:

        res = []

        while matrix:
            # 1. 取上层
            res += matrix.pop(0)

            # 2. 取右
            if matrix:
                right = [l.pop() for l in matrix]
                res += right
            # 过滤空列表元素
            if len(matrix)==0 or len(matrix[0])==0:
                break
            # 3. 取下
            if matrix:
                down = matrix.pop()[::-1]
                res += down

            # 4. 取左
            if matrix:
                left = [l.pop(0) for l in matrix][::-1]
                res += left
            if len(matrix) == 0 or len(matrix[0]) == 0:
                break
        return res

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(Solution().spiralOrder(matrix))
