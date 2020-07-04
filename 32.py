class Solution:
    """
    使用一个栈，遇到（ 就入栈，遇到 ），判断栈是否为空，为空时直接舍去该字符，不为空时取出一个（ ，
    多余的）会重置参数lastIndex, lastRes
    """
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = [-1] # 栈的起始元素，用于利用索引计算个数
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif len(stack)>1: # stack 内有起始元素,
                stack.pop()
                res = max(res, i - stack[-1])
            else:#
                stack[0] = 0
        return res
