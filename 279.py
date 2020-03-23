class Solution:
    # TODO: 该方法会超时
    def numSquares(self, n: int) -> int:
        if n==1:
            return 1

        memo = [-1] * (n+1)
        return self.findSquares(memo, n)

    def findSquares(self, memo: list, n: int) -> int:
        if memo[n] != -1:
            return memo[n]

        if ( int(n**0.5) )**2 == n:
            memo[n] = 1
            return 1

        tmp_min_len = n
        for i in range(int(n**0.5), 0, -1):
            if memo[n-i**2] != -1:
                tmp_min_len = min(tmp_min_len, memo[n-i**2] + 1 )
            else:
                tmp = self.findSquares( memo, n - i**2 )
                tmp_min_len = min( tmp_min_len, tmp + 1)
            if memo[n-i**2]==1:
                break

        memo[n] = tmp_min_len
        return tmp_min_len


class Solution2:
    #TODO：四平方定理
    def numSquares(self, n: int) -> int:

        if int( n ** 0.5 ) ** 2 == n:
            return 1

        for i in range(1, int(n ** 0.5)+1):
            rem = n - i ** 2
            if int( rem ** 0.5 ) ** 2 == rem:
                return 2

        while n % 4 == 0:
            n, _ = divmod(n, 4)

        if n>=7 and (n - 7) % 8 == 0:
            return 4
        else:
            return 3





res = Solution2().numSquares(2)
print(res)
