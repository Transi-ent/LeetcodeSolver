
def removeElement(nums: list, val):

    k, cur, n=0, 0, len(nums) # [0 ... k) sorted array

    while cur<n:

        if nums[cur]==val:

            if cur+1<n:
                nums[cur]=nums[cur+1]
                continue


        else:
            cur+=1
            k+=1

    for i in range(n-k):
        nums.pop()

    return len(nums)
