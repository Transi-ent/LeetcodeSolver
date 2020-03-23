def groupAnagrams(strs: list) -> list:
    """
    因为字母易位词所包含的字母都相同，可以建立一个字典
    键为排好序的该字母易位词字符串，值为该字符集组成的所有的字母易位词。
    :param strs:
    :return:
    """
    res, d = [], {}
    for s in strs:
        key = ''.join(sorted(s))
        if d.get(key):
            d[key].append(s)
        else:
            d[key] = [s]

    return list(d.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
