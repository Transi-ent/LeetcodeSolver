class Solution:
    """
    直接排序，利用语言内置的函数
    """
    def findKthLargest(self, nums: list, k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
import heapq
class Solution2:
    """
    1，设置一个包含 k 个元素的小顶堆；
    2，当堆内元素个数小于k时，直接往里面放；
    3，当堆内元素个数等于k时，若当前元素小于堆顶元素，直接丢弃，若当前元素大于堆顶元素，进行替换
    """
    def findKthLargest(self, nums: list, k: int) -> int:
        if len(nums)<k:
            raise Exception("k 值异常~")

        lyst = []
        for i in range(k):
            heapq.heappush(lyst, nums[i])

        for i in range(k, len(nums)):
            top = lyst[0]
            if nums[i]>top:
                heapq.heapreplace(lyst, nums[i])
        return lyst[0]
