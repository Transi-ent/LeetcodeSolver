class Solution:
    def isStraight(self, nums: list) -> bool:
        nums.sort()
        flag = True
        for i in range(1, 5):
            if nums[i]!=nums[i-1]+1:
                flag = False
                break
        if nums[0]!=0:# 当数组中不包含0时，直接返回判断是否连续的结果
            return flag

        # 统计0的个数
        times, start = 0, None
        for i, em in enumerate(nums):
            if em==0:
                times += 1
            else:
                start = i
                break
        map = {}
        for i in range(start, 5):
            if nums[i] in map:
                return False
            else:
                map[nums[i]] = 1
        for i in range(start+1, 5):
            if nums[i]-nums[i-1]==1:
                continue
            else:
                if nums[i]-nums[i-1]>times+1:
                    return False
                else:
                    times -= (nums[i]-nums[i-1]-1)
                    if times<0:
                        return False
        return True

print(Solution().isStraight([0,0,2,2,5]))
