class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.mins)==0 or x<=self.mins[-1]:
            self.mins.append(x)

    def pop(self) -> None:
        if self.stack[-1]==self.mins[-1]:
            self.mins.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.mins[-1] if self.mins else None
