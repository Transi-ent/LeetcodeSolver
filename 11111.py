def f(grid: list)->int:
    """
    :param grid: grid[list[]], list内，0为空位，1为甲方棋子，2为乙方
    :return: 0，1，2，3 --> 甲胜，乙胜，平局，未结束。
    """
    stat = 0
    crossSum1, crossSum2 = 0, 0
    for i in range(3):
        stat += sum([s!=0 for s in grid[i]])

        crossSum1 += grid[i][i]
        crossSum2 += grid[i][2-i]

        tmp = sum(grid[i])
        # 判定存在整行胜的棋子
        if tmp>0 and tmp%3==0:
            if grid[i][0]==1:
                return 0
            else:
                return 1
        # 判断存在成列胜
        tmp2 = grid[0][i] + grid[1][i] + grid[2][i]
        if tmp2>0 and tmp2%3==0:
            if tmp2==3:
                return 0
            else:
                return 1

    if crossSum1>0 and crossSum1%3==0:
        return 0 if crossSum1==3 else 1
    if crossSum2>0 and crossSum2%3==0:
        return 0 if crossSum2==3 else 1

    if stat==9:
        return 2
    else:
        return 3
