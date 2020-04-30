def isHappy( n: int) -> bool:

    s = set([n])
    while n>1:
        n = sum([int(i)**2 for i in str(n)])

        if n in s:
            return False
        else:
            s.add(n)

    return n==1

def isHappy2( n: int) -> bool:

    s = set([n])
    while n>1:
        tmp = 0
        while n>=10:
            n, m = divmod(n, 10)
            tmp += m**2

        tmp += n**2
        n = tmp
        if n in s:
            return False
        else:
            s.add(n)

    return n==1

class Solution:
    """
    使用字符串 + 列表表达式
    """
    def isHappy(self, n: int) -> bool:
        loopSet = set()
        while n != 1:
            if n in loopSet:
                return False

            loopSet.add(n)
            n = sum([int(i)**2 for i in str(n)])

        return True

class Solution2:
    """
    求出一个数每个数位的平方和
    """
    def isHappy(self, n: int) -> bool:
        def sumOfSquareDigit(n: int)->int:
            SUM = 0
            while n>9:
                n, rem = divmod(n, 10)
                SUM += rem**2
            return SUM + n**2
        loopSet = set()
        while n!=1:
            if n in loopSet:
                return False

            loopSet.add(n)
            n = sumOfSquareDigit(n)

        return True
