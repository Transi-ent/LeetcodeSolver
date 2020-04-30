class Solution:
    """
    只出现一个重复的数字，且数字都在 [1 ... n] 之间，
    在一个引用链中，如果出现了一个环，那么环的入口节点将会有 >=1 个前驱；
    因为这个长为 n+1 的数组元素都在 1 ... n 之间，那么从索引 0 开始搜索，起点元素不可能为0，
    所以不可能出现元素对应自己本身索引的情况。
    「使用双指针 —— 快慢指针，」，先做【142】号题，再过来
    """
    def findDuplicate(self, nums: list) -> int:
        fast, slow = 0, 0
        # 得到两个指针在第一次相遇点
        while True:
            print("fast={}, slow={}".format(fast, slow))
            fast, slow = nums[nums[fast]], nums[slow]

            if nums[fast]==nums[slow]:
                break

        print("nums[fast]=", nums[fast])
        # 第二次相遇时所在的点即为环的入口节点
        fast = 0
        while nums[fast] != nums[slow]:
            fast, slow = nums[fast], nums[slow]

        print(nums[fast])
        return nums[fast]


Solution().findDuplicate([1,2,3,4,2])
