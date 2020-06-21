class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff# 将大于32位整型的数字进行截取
        a, b = a&x, b&x
        while b:
            a, b = a^b, ((a&b)<<1)&x # 分别求取进位和与非进位和并进行赋值，
                                    # 为了防止左移过程中超出32位整型，需要进行截取
        return a if a<=0x7fffffff else ~(a^x)# 因为正数最大的补码为0x7fffffff，
                            # 大于该数时表明该数字为负数，需要进行还原处理。
                            # a^x操作相当于取反，~(a^x)是对Python中数据的还原
