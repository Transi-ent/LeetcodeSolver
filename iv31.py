class Solution:
    """
    直接模拟入栈和出栈的过程。结果是唯一确定的；
    若模拟结束时，栈不为空，说明有误
    """
    def validateStackSequences(self, pushed: list, popped: list) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1]==popped[i]:
                stack.pop()
                i += 1
        return not stack


print(Solution().validateStackSequences([2,1,3,0], [1,0,3,2]))
