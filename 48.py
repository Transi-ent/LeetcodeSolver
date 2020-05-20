class Solution:
    """
    就像洋葱一样，让他们一层一层的旋转
    """
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)//2): # i 为可取的层数（从外层开始数）
            # 旋转元素
            for j in range(i, len(matrix)-i-1): # j 为可取的列数（以上层元素为标准）

                matrix[i][j], matrix[j][-(i+1)], matrix[-(i+1)][-(j+1)], matrix[-(j+1)][i] = \
                matrix[-(j + 1)][i], matrix[i][j], matrix[j][-(i+1)], matrix[-(i+1)][-(j+1)]


matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
Solution().rotate(matrix)
print(matrix)
