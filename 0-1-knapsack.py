def knapSack01(w: list, v: list, capacity: int) ->int:
    if len(w) == 0:
        return 0
    assert len(w)==len(v), 'weight数组和value数组具有相同的长度'

    # 将求解过程中的子问题结果存储在数组中
    # memo[i][j] 表示要考虑第 i 号物品在背包剩余容量为 j 的情况下，
    # ...背包可存放的最大容量
    memo = [ [0]*(capacity+1) for _ in range(len(w)) ]
    # 初始化 memo
    for j in range( 1+capacity):
        memo[0][j] = 0 if w[0]>j else v[j]

    for i in range(len(w)):
        for j in range(capacity+1):
            if j>w[i]:
                memo[i][j] = max(memo[i-1][j], v[i]+memo[i-1][j-w[i]])

    return memo[-1][-1]

def knapSack01_2(w: list, v: list, capacity: int) ->int:
    """
    压缩状态空间，使空间复杂度降到 O(2C), 时间复杂度仍为O(NC)，
    ...因为每次计算第 i 行状态时，仅会用到第 i-1 行，所以留下2行的
    ...状态空间即可
    :param w: n个物品的重量或者体积数组；
    :param v: n个物品的 values 数组
    :param capacity: 背包的总容积；
    :return:
    """
    if len(w) == 0:
        return 0
    assert len(w)==len(v), 'weight数组和value数组具有相同的长度'

    # 将求解过程中的子问题结果存储在数组中
    # memo[i][j] 表示要考虑第 i 号物品在背包剩余容量为 j 的情况下，
    # ...背包可存放的最大容量
    memo = [ [0]*(capacity+1) for _ in range(2) ]
    # 初始化 memo
    for j in range( 1+capacity):
        memo[0][j] = 0 if w[0]>j else v[j]

    for i in range(1, len(w)):
        for j in range(capacity+1):
            if j>w[i]:
                memo[i%2][j] = max(memo[(i-1)%2][j], v[i]+memo[(i-1)%2][j-w[i]])

    return memo[-1][-1]

def knapSack01_3(w: list, v: list, capacity: int) ->int:
    """
    继续压缩状态空间，使空间复杂度降到 O(C), 时间复杂度仍为O(NC)，
    ...因为每次计算第 i 行状态时，仅会用到第 i-1 行，如果从后往前
    ...更新的话，只需要留下一行即可
    :param w: n个物品的重量或者体积数组；
    :param v: n个物品的 values 数组
    :param capacity: 背包的总容积；
    :return:
    """
    if len(w) == 0:
        return 0
    assert len(w)==len(v), 'weight数组和value数组具有相同的长度'

    # 将求解过程中的子问题结果存储在数组中
    # memo[i][j] 表示要考虑第 i 号物品在背包剩余容量为 j 的情况下，
    # ...背包可存放的最大容量
    memo = [-1]*(capacity+1)
    # 初始化 memo
    for j in range( 1+capacity):
        memo[j] = 0 if w[0]>j else v[j]

    for i in range(1, len(w)):
        for j in range(capacity, -1, 0):
            if j>w[i]:
                memo[j] = max(memo[j], v[i]+memo[j-w[i]])

    return memo[-1][-1]
