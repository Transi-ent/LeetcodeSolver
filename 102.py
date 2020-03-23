# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list]:

        queue = [root]
        res = []
        while queue:
            currentLayer = queue
            #res.append()
            queue, layRes = [], []
            for node in currentLayer:
                layRes.append(node.val)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(layRes)

        return res
