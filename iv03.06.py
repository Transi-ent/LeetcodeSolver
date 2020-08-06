class AnimalShelf:

    def __init__(self):
        # self.code = 0 # 初始化编号
        self.data = []


    def enqueue(self, animal: list) -> None:
        self.data.append(animal)


    def dequeueAny(self) -> list:
        if not self.data:
            return [-1, -1]
        ret = self.data.pop(0)
        return ret


    def dequeueDog(self) -> list:
        ret = None
        for i, pet in enumerate(self.data):
            if pet[1]==1:
                ret = self.data.pop(i)
                break
        if ret is None:
            return [-1, -1]
        return ret


    def dequeueCat(self) -> list:
        ret = None
        for i, pet in enumerate(self.data):
            if pet[1] == 0:
                ret = self.data.pop(i)
                break
        if ret is None:
            return [-1, -1]
        return ret
