class Solution:
    """
    没有更好的办法，先暴力解
    将二维列表展为一维，排序，取出第k个
    """
    def kthSmallest(self, matrix: list, k: int) -> int:
        lyst = []
        for row in matrix:
            lyst = lyst + row
        lyst.sort()
        print(lyst)
        return lyst[k-1]

    def kthSmallest2(self, matrix: list, k: int) -> int:
        """
        TODO: 官方题解真的牛皮，学到了
        :param matrix:
        :param k:
        :return:
        """
        return sorted(sum(matrix, []))[k-1]

class Solution2:
    """
    二分查找法：
    一直该矩阵有序，左上角值最小，右下角值最大，mid值基本上在副对角线上
    """
    def kthSmallest(self, matrix: list, k: int) -> int:
        n = len(matrix)
        def checkMid(mid)->bool:
            """
            以mid为分隔值时，左上角的元素个数是否不少于k个
            :param mid:
            :return:
            """
            i, j = n-1, 0 # 每次进行搜索的起点为左下角 matrix[n-1][0]
            num = 0 # 用于记录整个矩阵中，以mid值为分隔值时左上角元素个数
            while i>=0 and j<n:
                if matrix[i][j]<=mid:
                    num += i+1
                    j += 1
                else:
                    i -= 1
            return num >= k
        left, right = matrix[0][0], matrix[-1][-1]
        while left<right:
            mid = (left + right) // 2
            if checkMid(mid):
                right = mid
            else:
                left = mid + 1
        return left


matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]

print(Solution2().kthSmallest(matrix, 8))
