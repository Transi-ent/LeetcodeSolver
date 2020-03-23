def findRelativeRanks( nums: list) -> list:
    nums_s = sorted(nums, reverse=True)

    for i, num in enumerate(nums):
        ind = nums_s.index(num)
        if ind==0:
            nums[i]='Gold Medal'
        elif ind==1:
            nums[i] = 'Silver Medal'
        elif ind==2:
            nums[i] = 'Bronze Medal'
        else:
            nums[i]=str(ind+1)

    return nums


print(findRelativeRanks([5,4,3,2,1]))
