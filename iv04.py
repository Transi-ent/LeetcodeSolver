class Solution:
    """
    将二分搜索法进行拓展，拓展到二维空间
    """
    def findNumberIn2DArray(self, matrix: list, target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        if m==1:
            return target in matrix[0]
        else:
            return self.bs2D(matrix, target, 0, 0, m-1, n-1)


    def bs2D(self,matrix: list, target: int, lr: int, lc: int, hr: int, hc: int)->bool:
        """
        :param matrix: 搜索域
        :param target: target 值
        :param lr: 当前搜索行
        :param lc: 当前搜索列
        :param hr: 最大行号
        :param hc: 最大列号
        :return:
        """
        # 在 Matrix 的 [lr, hr] 行， [lc, hc] 列进行搜索，确认目标值的位置

        while lr<=hr and lc<=hc:
            print("({},{}) ({},{})".format(lr, lc, hr,hc))

            if target>matrix[lr][-1]:
                lr += 1
                lc, hc = 0, len(matrix[0])-1
                print("==1==")
                continue
            elif target< matrix[lr][0]:
                print("==2==")
                return False
            else:
                print("==3==")
                if hc - lc <=2:
                    if target in matrix[lr][lc: hc+1]:
                        return True
                    else:
                        lr += 1
                        lc, hc = 0, len(matrix[0])-1
                        continue
                mc = (lc+hc)//2
                if matrix[lr][mc] == target:
                    return True
                if matrix[lr][mc] > target:
                    hc = mc - 1
                else:
                    lc = mc + 1
        return False



A = [[1,6,6,9,14,14,17],
     [5,8,9,9,14,17,18],
     [5,10,11,12,18,18,20],
     [5,15,16,16,20,23,27],
     [7,15,19,21,22,24,31],
     [12,16,22,22,24,25,34],
     [16,21,23,26,26,30,37],
     [18,25,25,30,33,36,37],
     [22,30,31,33,34,39,42]]

res = Solution().findNumberIn2DArray(A, 5)
print(res)
