def topKFrequent( nums: list, k: int) -> list:
    from collections import Counter

    c = Counter(nums)

    return [em[1] for em in c.most_common(k)]

def topKFrequent2( nums: list, k: int) -> list:

    d = {}

    for num in nums:
        d[num] = d.get(num, 0) + 1

    dd = list( d.items() )

    lyst = sorted(dd, key=lambda x: x[1], reverse=True)
    lyst[:] = [em[0] for em in lyst]

    return lyst[:k]
