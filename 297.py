# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
    一棵树的下边缘是被None值包裹着的。
    """
    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str, 官渡优先搜索，每个节点值都用空格隔开；
        """
        res = ""
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                res += str(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res += "n"
            res += " "
        return res

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        tree = data.split()
        if tree[0] == 'n':
            return None
        root = TreeNode(int(tree[0]))
        queue = [root]
        i = 1
        while queue:
            root = queue.pop(0)
            if root is None:# 相当于剪枝操作，对于已经为None的节点，不再继续处理其子节点
                continue
            root.left = TreeNode(int(tree[i])) if tree[i]!="n" else None
            root.right = TreeNode(int(tree[i+1])) if tree[i+1]!="n" else None
            i += 2
            queue.append(root.left)
            queue.append(root.right)
        return root

def printNode(root: TreeNode):
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)

# Your Codec object will be instantiated and called as such:
codec = Codec()
root = TreeNode(-1)
root.left = TreeNode(0)
ret = codec.deserialize(codec.serialize(root))
printNode(ret)
