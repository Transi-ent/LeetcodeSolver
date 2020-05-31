# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    使用中序遍历，得到按大小排序的数组，取出第k个节点值
    缺点：空间复杂度O(N)，没必要，使用一个常量记录一下次序就好
    """
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        lyst = []
        self.inorder(root, lyst)
        return lyst[k-1]

    def inorder(self, root: TreeNode, lyst: list):
        if root is None:
            return

        if root.left:
            self.inorder(root.left, lyst)

        lyst.append(root.val)

        if root.right:
            self.inorder(root.right, lyst)

class Solution2:
    """
    使用中序遍历，得到按大小排序的数组，取出第k个节点值
    TODO：使用迭代器，经常看看别人的题解，有时候真的是有想磕头的感觉
    """
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def gen(root: TreeNode):
            if root is not None:
                yield from gen(root.left)
                yield root.val
                yield from gen(root.right)

        ite = gen(root) # 返回该 BST 的最小的节点值
        for _ in range(k):
            res = next(ite)

        return res

