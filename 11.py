class Solution:
    def maxArea(self, height: list) -> int:
        """
        TODO: 能够盛水的体积在于两个索引之差的绝对值和两个墙中较低的那堵墙
        TODO：所以在使用对撞指针时尽量将指向矮墙的指针向内移动
        :param height:
        :return:
        """
        left, right = 0, len(height)-1
        area = 0

        while left<right:
            h = min(height[left], height[right])
            tmp = h * (right-left)
            if tmp>area:
                area = tmp

            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return area

class Solution2:
    """
    双指针 —— 对撞指针
    """
    def maxArea(self, height: list) -> int:
        left, right = 0, len(height)-1
        res = 0
        while left<right:
            res = max(res, (right-left)*min(height[left], height[right]))
            if height[left]>height[right]:
                right -= 1
            else:
                left += 1

        return res
