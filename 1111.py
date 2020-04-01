class Solution:
    """
    已知输入 seq 为有效的括号字符串，
    可以使用一个栈，将括号依次放入栈内，并同时使用一个变量记录
    ...栈的深度，所填入栈的元素根据入栈时是奇数深度还是偶数深度
    ...分别输出不同的值。
    """
    def maxDepthAfterSplit(self, seq: str) -> list:
        stack = []
        depth = 0
        res = []
        for em in seq:
            if em=="(":
                stack.append('(')
                depth += 1
                res.append( (depth+1)%2 )
            elif em==")":
                res.append((depth + 1) % 2)
                depth -= 1

        #print(res)
        return res


Solution().maxDepthAfterSplit()
