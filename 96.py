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

Solution().numTrees(6)
