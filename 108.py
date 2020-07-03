# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        def buildBST(l: int, r: int) ->TreeNode:
            """
            [l, r] 是一个左闭右闭的区间，表示索引取值范围
            """
            if l>r:
                return None
            mid = l + (r-l)//2
            node = TreeNode(nums[mid])
            node.left = buildBST(l, mid-1)
            node.right = buildBST(mid+1, r)
            return node
        return buildBST(0, len(nums)-1)
