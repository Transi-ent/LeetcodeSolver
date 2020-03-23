class Solution:
    """
    将 cookie 数列和 children 数列排序，然后依次计算
    """
    def findContentChildren(self, g: list, s: list) -> int:
        g.sort()
        s.sort()
        childP, cookieP, res = 0, 0, 0
        gl, sl = len(g), len(s)
        while childP<gl and cookieP<sl:
            if g[childP]<=s[cookieP]:
                res += 1
                childP += 1
                cookieP += 1
            else:
                cookieP += 1

        return res
