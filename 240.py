class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        if m==1:
            return target in matrix[0]
        else:
            return self.bs2D(matrix, target, 0, 0, m-1, n-1)
    def bs2D(self,matrix: list, target: int, lr: int, lc: int, hr: int, hc: int)->bool:
        while lr<=hr and lc<=hc:
            if target>matrix[lr][-1]:
                lr += 1
                lc, hc = 0, len(matrix[0])-1
                continue
            elif target< matrix[lr][0]:
                return False
            else:
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
