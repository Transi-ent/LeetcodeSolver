#! -*- encoding UTF-8 -*-

def moveZeros(nums):
    """
    将数组中的0移动到数组的最后
    :param nums:
    :return:
    """
    nonZeros=[]
    for i in nums:
        if i:
            nonZeros.append(i)

    for i in range(len(nonZeros)):
        nums[i] = nonZeros[i]

    for j in range(len(nonZeros), len(nums)):
        nums[j]=0

def moveZeros2(nums):

    r, cur=0, 0

    while cur<len(nums):

        if nums[cur]:
            nums[r] = nums[cur]
            r+=1

        cur+=1

    for i in range(r, len(nums)):
        nums[i] = 0


def moveZeros3(nums):

    r = 0

    for i in range(len(nums)):
        if nums[i]:
            if r!=i:
                nums[i], nums[r] = nums[r], nums[i]

        r+=1 

