def fib(N: int) -> int:
    print('N: ', N)
    memo = [-1]*(N+1)
    print(len(memo))
    memo[0]=0
    if N>0:
        memo[1]=1
    def fib2(n):

        if n==0:
            return 0
        if n==1:
            return 1

        if memo[n]!=-1:
            return memo[n]
        else:
            # memo[n]==-1
            memo[n]=fib2(n-1)+fib2(n-2)
        return memo[n]

    return fib2(N)

print(fib(2))
