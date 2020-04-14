# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    已知中序遍历是得到有序的列表，
    则反向的中序遍历可决此题
    """
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.convert(root, 0)
        return root

    def convert(self, root: TreeNode, num: int)->int:
        if root is not None:

            num = self.convert(root.right, num)

            root.val += num
            num = root.val

            num = self.convert(root.left, num)

            return num


        return 0

class Solution2:
    """
    """
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.inorder(root, 0)
        return root
    def inorder(self, root: TreeNode, n: int)->int:
        if root:
            if root.right:
                n = self.inorder(root.right, n)
            root.val += n
            n = root.val
            if root.left:
                n = self.inorder(root.left, n)

            return n
        return 0

def dfs(root: TreeNode):
    if root:
        print(root.val)
        dfs(root.left)
        dfs(root.right)

r = TreeNode(5)
r.left = TreeNode(2)
r.right = TreeNode(13)
root = Solution2().convertBST(r)
dfs(root)
#
#
# root = TreeNode(5)
# root.left = TreeNode(2)
# root.right = TreeNode(13)
# Solution().convertBST(root)
