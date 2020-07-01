class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> list:
        res = []
        def find(root: TreeNode, k: int, tmpLyst: list):
            if root is None:
                return
            if root.left is None and root.right is None:
                if root.val == k:
                    copyTmp = tmpLyst.copy()
                    copyTmp.append(k)
                    res.append(copyTmp)
                return
            tmpcopy = tmpLyst.copy()
            tmpcopy.append(root.val)
            find(root.left, k-root.val, tmpcopy)
            find(root.right, k-root.val, tmpcopy)
            return
        find(root, sum, [])
        return res

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(1)
print(Solution().pathSum(root, 1))
