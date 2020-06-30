class CQueue:
    """
    使用 stack 实现队列
    1，使用2个stack，当追加数据的时候，放在one里面；
    2，当删除数据的时候，直接从two删除，若two为空，则先将one中数据转到two中再删除，若one和two中都没有数据，返回-1；
    """
    def __init__(self):
        self.one = []
        self.two = []

    def appendTail(self, value: int) -> None:
        self.one.append(value)

    def deleteHead(self) -> int:
        if len(self.two)!=0:
            return self.two.pop()
        # len(self.two)==0
        if len(self.one)==0:
            return -1
        # len(self.two)==0 and len(self.one)!=0
        while self.one:
            self.two.append(self.one.pop())
        return self.two.pop()
