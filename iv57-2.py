class Solution:
    """
    超时解法
    """
    def findContinuousSequence(self, target: int) -> list:
        def genSequence(mid: int, n: int):
            if n%2==1:
                return list(range(mid-(n//2), mid+(n//2)+1))
            elif n%2==0:
                return list(range(mid-(n//2)+1, mid+(n//2)+1))
        res = []
        for n in range(2, target//2):

            mid = target//n
            tmp = genSequence(mid, n)
            if tmp[0]>0 and sum(tmp)==target:
                res.append(tmp)

        return sorted(res, key=lambda x: x[0])

class Solution2:
    """
    利用等差数列的公式
    """
    def findContinuousSequence(self, target: int) -> list:
        def genSequ(start: int, n: int):
            return list(range(start, start+n))
        res = []
        for n in range(2, target//2+1):
            tmp = target - (n-1)*n/2
            if tmp%n==0 and tmp//n>0:
                start = int(tmp//n)
                lyst = genSequ(start, n)
                res.append(lyst)
        return sorted(res, key=lambda x: x[0])


res = Solution2().findContinuousSequence(15)
print(res)
