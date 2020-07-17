class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    # 维护一个有序数组，这样中位数更好求
    def addNum(self, num: int) -> None:
        n = len(self.data)
        if n==0:
            self.data.append(num)
            return
        elif num<self.data[0]:
            self.data.insert(0, num)
            return
        elif num>=self.data[-1]:
            self.data.append(num)
            return

        # 当数组不为空，且按序应该在数组中间时
        left, right = 0, n-1
        while left<right:
            mid = (left+right)//2
            if self.data[mid]==num:
                self.data.insert(mid, num)
                return
            elif self.data[mid]<num:
                left = mid + 1
            else:
                right = mid - 1
        # 从right的位置向右搜索找到第一个大于num的数字的索引
        while self.data[right]<num:
            right += 1
        self.data.insert(right, num)

    def findMedian(self) -> float:
        print(self.data)
        n = len(self.data)
        if n&1:
            return self.data[n//2]
        else:
            return (self.data[n//2 - 1]+self.data[n//2])/2

med = MedianFinder()
med.addNum(12)
med.addNum(10)
med.addNum(13)
med.addNum(11)
print(med.findMedian())
print(med.findMedian())
