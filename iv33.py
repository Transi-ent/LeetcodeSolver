class Solution:
    """
    【给定一个序列，判定该序列是不是一棵BST经过后续遍历得到的】
    【思路】：
    1，利用 BST 的递归结构特点，使用递归解决；
    2，后续遍历：先处理左子树——> 右子树 ——> 根节点；
    3，因此，得到的后续遍历的序列为，list, list[:m]为左子树， list[m:-1]为右子树，
        list[-1]为根节点 (m为list从左往右遍历得到的第一个大于list[-1]的值的索引)；
    """
    def verifyPostorder(self, postorder: list) -> bool:
        def recur(i, j)->bool: # 利用Python闭包，i，j 表示列表值的索引
            if i>=j: return True
            p = i
            while postorder[p]<postorder[j]:
                p += 1 # 利用所有左子树节点值小于根节点的性质，找出第一个大于根节点的值，用以划分区间
            m = p # 找到划分区间的索引值
            while postorder[p]>postorder[j]:
                p += 1 # 利用所有左子树节点值小于根节点的性质, 判定该树正确性
            return p==j and recur(i, m-1) and recur(m, j-1) #短路性质可以剪枝
        return recur(0, len(postorder)-1)


print(Solution().verifyPostorder([1,6,3,2,5]))
