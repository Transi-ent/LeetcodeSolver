class Solution:
    def minNumber(self, nums: list) -> str:
        def compare(s1: str, s2: str)->bool:
            """
            如果s1大返回True，否则返回False
            :param s1:
            :param s2:
            :return:
            """
            if s1==s2: return True

            n1, n2 = len(s1), len(s2)
            n = min(n1, n2)
            for i in range(n):
                if s1[i]>s2[i]:
                    return True
                elif s1[i]<s2[i]:
                    return False
            # 当s1 与 s2 的前n个字符相同时
            if n1>n:
                return compare(s1[n:], s2)
            else:
                return compare(s1, s2[n:])

        nums = [str(i) for i in nums]
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if compare(nums[i], nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]

        return ''.join(nums)

class Solution2:
    def minNumber(self, nums: list) -> str:
        def compare(s1: str, s2: str)->bool:
            """
            如果s1大返回True，否则返回False
            :param s1:
            :param s2:
            :return:
            """
            if s1+s2>s2+s1:
                return True
            else:
                return False

        nums = [str(i) for i in nums]
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if compare(nums[i], nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]

        return ''.join(nums)

print(Solution2().minNumber([999999998,999999997,999999999]))

#print(compare('999999998', '999999997'))
