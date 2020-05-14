class Solution:
    """
    给定一个数组，将该数组原地改为按照字典序排成的下一个更大的排列；
    即可以将该数组想象为一个数，每个元素是该数组对应的数上的数字，需要对当前的数进行改动，
    ...得到下一个更大的数，使得该数是大于原来的数中最小的，且知有序数组是最小排列。
    例如 [1,2,3,4,5,6]
    123456
    123465
    123546
    123564
    123645
    123654
    ...
    654321
    1，首先找到第一个升序对（nums[i], nums[j]）.
    2，从 j 开始之后的部分从后往前找第一个 大于 nums[i] 的数 nums[k]
    3，交换nums[i], nums[k] 的位置；
    4，对子数组 nums[j: ] 排序
    """
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ii = jj = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i]<nums[i+1]:
                ii = i
                break
        print('ii=', ii)
        for i in range(len(nums)-1, ii, -1):
            if nums[i]>nums[ii]:
                jj = i
                break
        if ii==-1 and jj==-1:
            nums = nums[::-1]
        nums[ii], nums[jj] = nums[jj], nums[ii]
        self.quickSort(nums, ii+1, len(nums)-1)


    def quickSort(self, nums: list, i: int, j: int):
        if i>=j:
            return
        pv = nums[i] # Pivot value 枢轴元素
        ii, jj, cur = i, j+1, i+1 # nums[i: ii] 中所有元素<=pv, nums[jj: j] 中所有元素> pv
        while cur<jj:
            if nums[cur]<=pv:
                ii += 1
                cur += 1
            else:
                jj -= 1
                nums[jj], nums[cur] = nums[cur], nums[jj]

        nums[i], nums[ii] = nums[ii], nums[i]
        self.quickSort(nums, i, ii-1)
        self.quickSort(nums, jj, j)





nums = [3,2,1]
Solution().nextPermutation(nums)
print(nums)






# for i in range(10, 0, -1):
#     print(i, end=', ')
