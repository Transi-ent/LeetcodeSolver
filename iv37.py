# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
    使用了一个状态量存储根节点，没有进行编解码，捷径
    """
    def __init__(self):
        self.root = None

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        self.root = root
        return None

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        return self.root

class Codec2:

    def serialize(self, root):
        """Encodes a tree to a single string.
        使用层序遍历，利用队列
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        res = str(root.val)
        q = [root.left, root.right]
        while q:
            node = q.pop(0)
            if node:
                res += ','+str(node.val)
                q.extend([node.left, node.right])
            else:
                res += ',N'
        return res


    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        当往一个队列中放入root.left 时，从队列中取出该节点时会直接取出left的节点标记，而不会与root建立父子关系
        -> 正确的姿势应该是直接存放 root，进行操作时取出root，对 root.left 进行操作；
        :type data: str
        :rtype: TreeNode
        """
        if data=='':
            return None
        lyst = data.split(',')

        root = TreeNode(int(lyst[0]))
        i = 1
        nodes = [root]
        while nodes:
            node = nodes.pop(0)
            if lyst[i] !='N':
                node.left = TreeNode(int(lyst[i]))
                nodes.append(node.left)

            i += 1
            if lyst[i] != 'N':
                node.right = TreeNode(int(lyst[i]))
                nodes.append(node.right)

            i += 1
        return root


def printTree(root: TreeNode):
    if root is None:
        print("null")
    q = [root]
    while q:
        node = q.pop(0)
        if node:
            print(node.val, ', ')
            q.extend([node.left, node.right])
        else:
            print("null, ")

code = Codec2()
printTree(code.deserialize(code.serialize(None)))
root = TreeNode(-1)
root.left = TreeNode(233)
#print(code.serialize(root))
printTree(code.deserialize(code.serialize(root)))
