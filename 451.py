def frequencySort( s: str) -> str:
    """
    1，统计字符频率(使用大顶堆)；
    2，从堆顶依次取出所有的元素；
    3，利用出现的元素和该元素出现的频次依次拼接结果
    :param s:
    :return:
    """
    d, res = {}, ''
    for ch in s:
        d[ch] = d.setdefault(ch, 0) + 1

    lyst = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for k, v in lyst:
        res += str(k) * v

    return res


"loveleetcode"
print(frequencySort("loveleetcode"))
