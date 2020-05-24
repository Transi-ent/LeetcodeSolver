class Solution:
    """
    1，先统计没重任务出现的次数；
    2，不断循环执行字典中的任务，直至字典为空。
    3，设置一个时钟，每执行一个任务或待命一个单位时间，时钟就+1
    """
    def leastInterval(self, tasks: list, n: int) -> int:

        freq = {}
        for tk in tasks:
            freq[tk] = freq.get(tk, 0) + 1

        coolDown = {}# 用于记录某一任务上次的冷却时间
        clock = 0
        while freq:
            for task, v in freq.items():
                if (not task in coolDown):
                    freq[task] -= 1
                    coolDown[task] = clock
                    clock += 1
                elif clock - coolDown[task] > n:
                    freq[task] -= 1
                    coolDown[task] = clock
                    clock += 1
                else:
                    # 冷却时间
                    clock += 1
                    break
            print("clock: {}, freq={}".format(clock, freq))

            freq = {k:v for k, v in freq.items() if v>0}
        print(clock)
        return clock

class Solution2:
    """
    1，先统计没重任务出现的次数；
    2，不断循环执行字典中的任务，直至字典为空。
    3，设置一个时钟，每执行一个任务或待命一个单位时间，时钟就+1
    """
    def leastInterval(self, tasks: list, n: int) -> int:
        if len(tasks)<=1 or n==0:
            return len(tasks)
        freq = {}
        for tk in tasks:
            freq[tk] = freq.get(tk, 0) + 1

        counts = list(freq.values())
        counts.sort()
        maxCount = counts[-1]
        retCount = (maxCount-1) * (n+1) + 1
        i = len(counts) - 2
        while i>=0 and counts[i]==maxCount:
            retCount += 1
            i -= 1
        print(retCount)
        return max(retCount, len(tasks))


tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
Solution2().leastInterval(tasks, 2)

