class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.minData = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.minData)==0 or x <= min(self.minData):
            self.minData.append(x)

    def pop(self) -> None:
        if self.data[-1]==self.getMin():
            self.minData.pop()
        self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.minData[-1]

stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
print(stack.getMin())
stack.pop()
print(stack.top())
print(stack.getMin())
