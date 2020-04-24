class Solution:
    """
    Brutal Force, 超时
    """
    def reversePairs(self, nums: list) -> int:

        n = len(nums)
        if n<2:
            return 0

        res = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i]>nums[j]:
                    res += 1
        return res

class Solution2:
    """
    归并排序，
    """
    def reversePairs(self, nums: list) -> int:
        n = len(nums)
        if n < 2:
            return 0
        tmp = [0]*n
        return self.mergeSort(nums.copy(), 0, n-1, tmp)

    def mergeSort(self, nums: list, left: int, right: int, tmp: list)->int:
        """
        对 [left ... right] 对左闭右闭区间进行归并排序。
        :param nums: 原输入数组
        :param tmp: 在归并过程中进行排序的数组
        :param left:
        :param right:
        :return:
        """
        if left>=right:
            return 0

        mid = left + (right - left)//2
        leftRes = self.mergeSort(nums, left, mid, tmp)
        rightRes = self.mergeSort(nums, mid+1, right, tmp)

        p1, p2 = left, mid+1
        res = 0
        cur = left
        while p1<=mid and p2<=right:
            if nums[p1]<=nums[p2]:
                tmp[cur] = nums[p1]
                p1 += 1
            else:
                tmp[cur] = nums[p2]
                p2 += 1
                res += mid - p1 + 1
                print("increment=", mid - p1 + 1)
            cur += 1
        if p1<=mid:
            tmp[cur: right+1] = nums[p1:mid+1]
        elif p2<=right:
            tmp[cur: right+1] = nums[p2:right+1]
        nums[left: right+1] = tmp[left: right+1]
        print("[{} ...{}... {}], leftRes={}, rightRes={}, res={}".format(left, mid, right, leftRes, rightRes, res))
        return res+leftRes+rightRes

res = Solution2().reversePairs([7,5,6,4])
print(res)










