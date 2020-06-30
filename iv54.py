class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    使用中序遍历取出所有节点，再返回第K大元素
    """
    def kthLargest(self, root: TreeNode, k: int) -> int:
        vals = []
        def inorder(root: TreeNode):
            if root is None:
                return
            inorder(root.left)
            vals.append(root.val)
            inorder(root.right)
            return
        inorder(root)
        return vals[-k]

class Solution2:
    """
    使用中序遍历倒序+在遍历过程中递减k
    """
    def __init__(self):
        self. k = 0
        self.res = 0
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k = k
        def inorder(root: TreeNode):
            if root is None:
                return
            inorder(root.right)
            self.k -= 1
            if self.k==0:
                self.res = root.val
                return
            inorder(root.left)
            return
        inorder(root)
        return self.res
