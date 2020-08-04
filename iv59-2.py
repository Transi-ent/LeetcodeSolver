class MaxQueue:
    """
    在一个队列中，当队列的最大值被pop出去后，如何保证进行后续的max_value() 操作还能得到正确的结果
    解决存放最大值的办法，可以将队列的最大值存放到一个双端队列中去里面
    """
    def __init__(self):
        self.data = []
        self.deque = []

    def max_value(self) -> int:# 最大值存放在双端队列的队首，deque[1]存放队列中的次最大值
        if not self.deque:
            return -1
        return self.deque[0]

    def push_back(self, value: int):
        self.data.append(value)
        while self.deque and self.deque[-1]<value:
            self.deque.pop()
        self.deque.append(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        ret = self.data.pop(0)
        if ret==self.deque[0]:
            self.deque.pop(0)
        return ret
