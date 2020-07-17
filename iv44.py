class Solution:
    def findNthDigit(self, n: int) -> int:
        if n<10:
            return n
        # 说明n至少为两位数
        weight = 90 # 代表在当前位数下，数字的个数（比如两位数有90个，3位数900个）
        number = 10 + weight*len(str(weight))
        while number<n:
            weight *= 10
            number += weight*len(str(weight))

        # 此时已经找到n 所在位置的上下限
        size = len(str(weight))
        start = 10**(size-1)
        # end = start*10 - 1

        n -= (number-size*(weight))
        a, b = n//size, n%size

        # while n>=size:
        #     n -= size
        #     start += 1

        print("n:{}, weight:{}, start:{}, a:{}, b:{}".format(n, weight, start, a, b))
        return int(str(start+a)[b])

print(Solution().findNthDigit(13))
