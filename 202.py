def isHappy( n: int) -> bool:

    s = set([n])
    while n>1:
        n = sum([int(i)**2 for i in str(n)])

        if n in s:
            return False
        else:
            s.add(n)

    return n==1

def isHappy2( n: int) -> bool:

    s = set([n])
    while n>1:
        tmp = 0
        while n>=10:
            n, m = divmod(n, 10)
            tmp += m**2

        tmp += n**2
        n = tmp
        if n in s:
            return False
        else:
            s.add(n)

    return n==1
