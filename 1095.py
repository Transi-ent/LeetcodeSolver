# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, lyst: list):
        self.lyst = lyst
    def get(self, index: int) -> int:
        return self.lyst[index]
    def length(self) -> int:
        return len(self.lyst)

class Solution:
    """
    先找出该数组的最大值，然后再在两个子区间内使用二分查找；
    """
    def findInMountainArray(self, target: int,
                            mountain_arr:MountainArray) -> int:

        long = mountain_arr.length()
        maxIdx = self.findBiggest(mountain_arr)
        print("maxIdx={}".format(maxIdx))
        left = self.binarySearch(0, maxIdx, mountain_arr, target, True)
        if left!=-1:
            return left
        right = self.binarySearch(maxIdx, long-1, mountain_arr, target, False)
        return right

    def findBiggest(self, mountain_arr: MountainArray) -> int:
        long = mountain_arr.length()
        left, right = 0, long-1

        while True:
            mid = left + (right - left)//2
            midVal = mountain_arr.get(mid)
            if mid-1>=0 and mid+1<long:
                leftVal = mountain_arr.get(mid-1)
                rightVal = mountain_arr.get(mid+1)
                if  midVal> leftVal and midVal>rightVal:
                    return mid
                elif leftVal > midVal:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if mid==0:
                    return 1
                else:
                    return long-2

    def binarySearch(self, l: int, r: int, mountain_arr: MountainArray, target: int, asc: bool)->int:

        while l<=r:
            mid = l + (r-l)//2
            midv = mountain_arr.get(mid)
            if target == midv:
                return mid

            if asc:
                if target < midv:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target < midv:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

    def binarySearchDes(self, l: int, r: int, mountain_arr: MountainArray, target: int)->int:
        while l<=r:
            mid = l + (r-l)//2
            midv = mountain_arr.get(mid)
            if target == midv:
                return mid
            elif target < midv:
                l = mid + 1
            else:
                r = mid - 1
        return -1

mArr = MountainArray([3,5,3,2,0])

res = Solution().findInMountainArray(3, mArr)
print(res)


