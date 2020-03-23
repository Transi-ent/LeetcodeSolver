
def convertToBase7( num: int) -> str:
    # 记录正负数
    negative = False
    if num<0:
        negative=True
        num = -num

    res = ''
    n = 0
    while num>=7:
        num, rem = divmod(num, 7)
        res = str(rem)+res

    res = str(num)+res
    if negative:
        res = '-'+res

    return res

print(convertToBase7(-7))
