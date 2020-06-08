class Solution:
    """
    等式方程的可满足性，使用并查集
    """
    def equationsPossible(self, equations: list) -> bool:
        def find(x):
            # 找出索引为 x 的元素的根为多少，根元素满足 parent[x] = x
            if x==parent[x]:
                return x
            else:
                parent[x] = find(parent[x])
                return parent[x]

        parent = [i for i in range(26)]# 对并查集初始化，每个元素的父亲都是自己
        ## 对于方程组中的等式情况
        for eq in equations:
            if eq[1]=="=":# 判定过程可剪枝
                # 找出等式两边元素的父母
                p1 = find(ord(eq[0])-ord('a'))
                p2 = find(ord(eq[-1])-ord('a'))
                parent[p2] = p1

        ## 对于方程式中的不等式情况
        for eq in equations:
            if eq[1]=='!':
                p1 = find(ord(eq[0]) - ord('a'))
                p2 = find(ord(eq[-1]) - ord('a'))
                if p1==p2:
                    return False

        return True

res = Solution().equationsPossible(["a==b","b!=c","a==c"])
print(res)



