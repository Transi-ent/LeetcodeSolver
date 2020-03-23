# remove duplicated from sorted Array

def removeElement(nums):

    k=-1 # [0 ... k] completed array

    for i in range(len(nums)):

        if nums[i]!=nums[k] or k==-1:
            k+=1
            nums[k]=nums[i]


    print(nums)
    return k+1

nums = [1,1,2]
print(removeElement(nums))
# 当要求数组中的相同元素值最多有两个时，可以利用已排序区间的最后一个索引与相同元素序列的最后一个索引相减，
# 判断是否大于2
