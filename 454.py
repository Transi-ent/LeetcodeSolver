"""
给定4个整形数组，找出使得i, j, k, l的总组合数，使得A[i]+B[j]+C[k]+D[l]=0
"""

# 1, brutal force, 4 layer for-loop O(N^4)

# 2, 3 layer for-loop, a check map, O(N^3)

def fourSum(A: list, B: list, C: list, D: list):

    # 2 2-layer for-loop, O(N^2)
    dSum, n = dict(), len(A)
    for i in range(n):

        for j in range(n):
            tmp = C[i]+D[j]
            if dSum.get(tmp):
                dSum[tmp]+=1

            else:
                dSum[tmp] = 1

    res = 0

    for i in range(n):

        for j in range(n):

            tmp = -(A[i]+B[j])

            if dSum.get(tmp):
                res+=dSum[tmp]


    return res




def fourSumCount( A: list, B: list, C: list, D: list) -> int:

    d1, res = {}, 0

    for i in range(len(A)):
        for j in range(len(B)):

            d1[A[i]+B[j]] = d1.get(A[i]+B[j], 0) + 1

    for i in range(len(C)):
        for j in range(len(D)):
            if d1.get(0-C[i]-D[j]):
                res += d1[0-C[i]-D[j]]

    return res























