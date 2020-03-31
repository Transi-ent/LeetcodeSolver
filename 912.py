class Solution:
    """
    Insertion Sort, 会超时
    """
    def sortArray(self, nums: list) -> list:

        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[j]<nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums


class Solution2:
    """
    Quick Sort
    """
    def sortArray(self, nums: list) -> list:
        self.quickSort(nums, 0, len(nums)-1)
        return nums

    def quickSort(self, nums: list, l: int, r: int)->list:
        if l>=r:
            return nums
        #print("nums: {}".format(nums))
        right = self.partition(nums, l, r)

        self.quickSort(nums, l, right-1)
        #print("left nums: {}".format(nums))

        self.quickSort(nums, right+1, r)
        #print("right nums: {}".format(nums))
        return nums

    def partition(self, nums, l: int, r: int)->int:
        """
        快排的 partition 操作就是找到隔板得位置，使得隔板的左边元素都
        大于枢轴元素，隔板的右边的元素都小于枢轴元素。且隔板放置之后整个
        区间的元素都符合隔板放置的要求。
        :param nums:
        :return:
        """
        # 取区间的第一个元素为枢轴元素，
        left, right = l, r+1
        p = nums[l]
        # nums[l+1 ... left] < p
        # nums[right ... r] >= p
        while left+1<right:
            if nums[left+1]<p:
                left += 1
            else:
                right -= 1
                nums[left+1], nums[right] = nums[right], nums[left+1]
        nums[l], nums[left] = nums[left], nums[l]
        # partition 完成后，left + 1 = right
        return left

class Solution3:
    """
    Merge Sort:
    先分，分到底不能继续再分了，就开始合
    """
    def sortArray(self, nums: list) -> list:
        return self.mergeSort(nums)

    def mergeSort(self, nums: list) -> list:
        if len(nums)<=1:
            return nums

        mid = len(nums)//2
        leftArr = self.sortArray(nums[:mid])
        rightArr = self.sortArray(nums[mid:])

        return self.merge(leftArr, rightArr)

    def merge(self, left: list, right: list) -> list:
        res = []
        i, j = 0, 0
        while i<len(left) and j<len(right):
            #print(left, '\n', right)
            if left[i]<=right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        res += left[i:]
        res += right[j:]
        return res

Solution3().sortArray([5,2,3,1])








