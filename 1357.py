class Cashier:

    def __init__(self, n: int, discount: int, products: list, prices: list):
        self.count = 0 # 用于记录当前客人的位次，用于给第n位顾客打折
        self.discount = discount
        self.n = n
        self.prices = {}
        for i in range(len(products)):
            self.prices[products[i]] = prices[i]

    def getBill(self, product: list, amount: list) -> float:
        self.count += 1
        size, cost = len(product), 0
        for i in range(size):
            cost += self.prices[product[i]] * amount[i]

        if self.count % self.n == 0:
            cost = cost - (self.discount*cost/100)
        return cost

cashier = Cashier(3, 50, [1,2,3,4,5,6,7],[100,200,300,400,300,200,100])
print(cashier.getBill([1,2], [1,2]))
print(cashier.getBill([3,7], [10,10]))
print(cashier.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]))
print(cashier.getBill([4],[10]))
print(cashier.getBill([7,3],[10,10]))
print(cashier.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]))
print(cashier.getBill([2,3,5],[5,3,2]))
