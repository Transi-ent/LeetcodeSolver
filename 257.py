# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        """
        使用两层函数，内层函数进行递归调用，返回所有节点值，
        外层函数处理所有节点值成为字符串
        :param root:
        :return:
        """
        global res
        res = list()

        if root is None:
            return []

        if root.left is None and root.right is None:
            return [str(root.val)]

        # lyst是一个存放str(num)的双层列表
        self._binaryTreePaths(root.left, [root.val])
        self._binaryTreePaths(root.right, [root.val])

        for i, lys in enumerate(res):
            res[i] = [str(k) for k in lys]

        res = ['->'.join(item) for item in res]

    def _binaryTreePaths(self, root: TreeNode, lyst: list):
        #TODO: python 函数参数的值传递，不纯粹，是浅拷贝
        # 如果该节点为 None 直接返回
        if root is None:
            return

        # 若该节点不为空，加入结果列表
        lyst.append(root.val)
        # 总是骂别人SB的人啊，为何总是要逞这个口舌之勇，不知道自己才是一个SB吗
        if root.left is None and root.right is None:
            res.append(lyst)

        self._binaryTreePaths(root.left, lyst)
        self._binaryTreePaths(root.right, lyst)


    def binaryTreePaths2(self, root: TreeNode) -> list:
        if root is None:
            return []
        lyst = []
        lyst[:] = self._binaryTreePaths2(root, lyst, '')
        lyst = [em[2:] for em in lyst]
        return lyst


    def _binaryTreePaths2(self, root: TreeNode, lyst: list, s: str) -> list:
        if root is None:
            return lyst

        if root.left is None and root.right is None:
            s += '->'
            s += str(root.val)
            lyst.append(s)
            return lyst
        else:
            s += '->'
            s += str(root.val)
            self._binaryTreePaths2(root.left, lyst, s)
            self._binaryTreePaths2(root.right, lyst, s)
            return lyst





