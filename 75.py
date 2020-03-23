# 数组中只有3个元素，对这个数组进行排序

def sortColors(nums):
    # 计数排序
    count = [0]*3

    for num in range(nums):
        count[num]+=1

    index=0
    es=[0, 1, 2]
    for e, freq in zip(es, count):

        for i in range(freq):
            nums[index]=e
            index+=1


def sortColors2(nums):
    # 三路快排，根据元素的取值将数组分为3份

    # [0 ... left], [left+1 ... right-1], [right ... len(nums)-1]
    n = len(nums)
    left, right, cur = -1, n, 0

    while cur<right:

        if nums[cur]==1:
            cur+=1

        elif nums[cur]<1:
            nums[cur], nums[left+1] = nums[left+1], nums[cur]
            left+=1
            cur+=1

        else:
            nums[cur], nums[right-1] = nums[right-1], nums[cur]
            right-=1


