# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        def buildBT(preorder: list, inorder: list) ->TreeNode:
            if len(preorder)==0:
                return None
            elif len(preorder)==1:
                return TreeNode(preorder[0])

            root = TreeNode(preorder[0])
            # index = map[preorder[0]]
            index = inorder.index(preorder[0])
            root.left = buildBT(preorder[1: 1+index], inorder[:index])
            root.right = buildBT(preorder[1+index: ], inorder[index+1:])
            return root

        if len(preorder) == 0:
            return None
        elif len(preorder) == 1:
            return TreeNode(preorder[0])

        return buildBT(preorder, inorder)

class Solution2:
    """
    重建一棵二叉树需要什么？
    根节点位置，左子树区间，右子树区间
    """
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        def buildBT(preRoot: int, left: int, right: int) ->TreeNode:
            """
            递归建立二叉树
            :param preRoot: 当前区间下的根节点索引(在前序遍历中)
            :param left: 在当前中序遍历索引区间下左边界
            :param right: 在当前中序遍历索引区间下右边界
            :return:
            """
            if left>right:
                return None
            if left==right:
                return TreeNode(inorder[left])

            index = map[preorder[preRoot]]
            root = TreeNode(preorder[preRoot])
            root.left = buildBT(preRoot+1, left, index-1)
            root.right = buildBT(preRoot+index-left+1, index+1, right)
            return root

        if len(preorder) == 0:
            return None
        elif len(preorder) == 1:
            return TreeNode(preorder[0])

        map = {}
        for i, num in enumerate(inorder):
            map[num] = i

        return buildBT(0, 0, len(inorder)-1)
