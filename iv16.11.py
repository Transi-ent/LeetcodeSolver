class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> list:
        res = []
        if k==0:
            return res
        if shorter==longer:
            return [shorter*k]
        for i in range(k, -1, -1):
            longth = shorter * i + longer * (k-i)
            res.append(longth)
        return res

print(Solution().divingBoard(1,2,3))
