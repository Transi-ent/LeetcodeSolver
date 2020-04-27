class Solution:
    """利用旋转排序的相对有序性，二分搜索。
    1、若 target 小于列首元素，大于列尾元素，则不存在；
    2、若大于列首元素，则 target 在左半边；
    3、若小于列首元素，则 target 在右半边；
    """
    def search(self, nums: list, target: int) -> int:

        if len(nums)<1 or (target<nums[0] and target>nums[-1]):
            return -1

        if target>=nums[0]:
            left = 0

        ### target 在 [left ... right] 该闭区间之内
        left, right = 0, len(nums)-1
        while left<=right:
            print("search interval: [{} {}], target={}".format(nums[left], nums[right], target))
            mid = left + ( right - left )//2
            print("mid={}".format(nums[mid]))
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                if target<nums[left]:
                    if nums[left]>nums[mid]:
                        right = mid-1
                    else:
                        left = mid + 1
                else:
                    right = mid - 1
            else:
                # target > nums[mid]
                if target>=nums[left]:
                    if nums[mid]<nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1

                else:
                    left = mid + 1
                # else:
                #     right = mid-1
        return -1

res = Solution().search([4,5,6,7,0,1,2], 0)
print(res)
