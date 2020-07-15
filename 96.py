class Solution:
    def numTrees(self, n: int) -> int:
        if n<3:
            return n

        memo = [-1] * n # memo[i] 用于存放有i+1个节点时，BST 的种数
        memo[ :2] = 1, 2

        for i in range(2, n): # 依次取出每一个需要求的数
            tmpRes = 0
            end = (i+1) // 2 if (i+1) % 2 == 0 else (i // 2) +1
            for j in range(end-1):
                if j==0:
                    tmpRes += 2 * memo[i-1]
                else:
                    tmpRes += 2 * ( memo[j-1] * memo[i-j-1] )
                    print("memo[j-1]={}, memo[i-j]={}".format(memo[j-1],memo[i-j]))
            print(memo)
            if (i+1)%2==0:
                tmpRes += 2*( memo[end-2]*memo[end-1] )
            else:
                print("i={}, end={}, tmpRes={}".format(i, end, tmpRes))
                tmpRes += memo[end-2]**2
            memo[i] = tmpRes

        print(memo)
        return memo[-1]

class Solution2:
    """
    使用记忆化搜索的方法，存储已经解决过的重复子问题。
    因为要求n 个节点组成的BST结构有多少种，假设该问题为f(n) = dp[n]
    （1）当n%2==1，(n-1)%2==0
    f(n) = [f(n-1)+f(n-2)+...f(n-1/2 +1)]*2 + f(n-1/2)
    (2) 当n%2==0，
    f(n) = [f(n-1)+f(n-2)+...f(n/2)]*2
    """
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[:2] = 1,1
        if n<2:
            return dp[n]

        # 不断填充数组，直至n
        for i in range(2, n+1):
            for small in range(0, i):
                big = i - 1 - small
                if small<big:
                    dp[i] += dp[big]*dp[small]*2
                elif small==big:
                    dp[i] += dp[big]*dp[small]
                else:
                    break

        return dp[-1]

print(Solution2().numTrees(6))
