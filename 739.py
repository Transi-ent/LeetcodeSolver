class Solution:
    """
    Brutal Force
    """
    def dailyTemperatures(self, T: list) -> list:
        res = []
        n = len(T)
        for i in range(n-1):
            for j in range(i+1, n):
                if T[j]>T[i]:
                    res.append(j-i)
                    break

            if i+1>len(res):
                res.append(0)

        res.append(0)
        print(res)
        return res

class Solution2:
    """
    利用递减栈，栈内元素从栈底到栈顶依次减小。
    每个元素只入栈和出栈一次，所以时间复杂度为 O(N)
    """
    def dailyTemperatures(self, T: list) -> list:
        n = len(T)
        queue = []
        res = [0 for _ in range(n)]
        for i, t in enumerate(T):
            # 当栈不为空 或者 当前温度大于栈顶温度时
            while len(queue)>0 and t > T[queue[-1]]:
                pre = queue.pop()
                res[pre] = i - pre
                # print("index: {}, value: {}".format(pre, i-pre))

            queue.append(i)
        # print(res)
        return res


Solution2().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
