def checkPerfectNumber(num: int) -> bool:
    #TODO: 超时
    factors = []

    for i in range(1, (num//2)+1):
        if num%i==0:
            factors.append(i)

    return sum(factors)==num

def checkPerfectNumber2(num: int) -> bool:
    factors = []

    for i in range(1, int(num**0.5)+1):
        if num%i==0:
            factors.append(i)
            factors.append(num//i)

    return sum(factors)==num*2




print(checkPerfectNumber2(28))
