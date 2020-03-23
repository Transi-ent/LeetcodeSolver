
def findWords( words) -> list:
    res = []
    dic = {1: 'qwertyuiop',
           2: 'asdfghjkl',
           3: 'zxcvbnm'}

    for i in range(len(words)):
        word = words[i]
        if len(word)==1:
            res.append(word)
            continue
        tmp = []
        for j in range(len(word)):

            # 取出该单词在该索引位置上字母属于第几行
            line = 0
            if word[j].lower() in dic[1]:
                line = 1
            elif word[j].lower() in dic[2]:
                line = 2
            else:
                line = 3

            tmp.append(line)
            print(tmp)
            # 对于第二个及以后的字母，如果他们不属于同一行，直接看下一个单词
            if 0<j :
                if line!=tmp[j-1]:
                    break
                # 连续两个相等
                # 如果为最后一个字母，则将该单词放入结果列表, 否则不用管，TODO：要注意只有一个字母单词的情况
                if j==len(word)-1:
                    res.append(word)

    return res
def findWords2( words) -> list:
    """
    利用集合的交集进行求解
    :param words:
    :return:
    """
    s1 = set('qwertyuiopQWERTYUIOP')
    s2 = set('asdfghjklASDFGHJKL')
    s3 = set('zxcvbnmZXCVBNM')

    res = []
    for i in range(len(words)):
        ws = set(words[i])
        if ws&s1==ws or ws&s2==ws or ws&s3==ws:
            res.append(words[i])

    return res







res = findWords2(["Hello", "Alaska", "Dad", "Peace"])
print(res)
