class Solution1:
    """
    使用 异或运算 的话，得到的结果是那两个只出现一次数字的异或值。
    （1）进行分组：分成2各组，出现一次的数字在 2 个不同的组里面。
        ... 出现两次的数字的两个相同的数字要在一个组里面；

    (2) 如何确保能够得到这样的分组呢？找到那两个只出现一次的数字，找到他们一个不同的
        二进制位（在该位上，一个数为0，一个数为1）
    """
    def singleNumbers(self, nums: list) -> list:
        ret = 0
        a, b = 0, 0

        for i in nums:
            ret ^= i

        bit = 1 # 从低位到高位开始找
        while ret&bit==0:
            bit <<=1

        for i in nums:
            if i&bit==0:
                a^=i
            else:
                b^=i
        print(a,b)
        return [a,b]
Solution1().singleNumbers([1,2,3,1,2,3,4,5])
