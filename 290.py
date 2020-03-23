def wordPattern( pattern: str, s: str) -> bool:
    l1 = [ch for ch in pattern]
    r1 = ''.join([str(l1.index(i)) for i in l1])
    # print(l1)
    #r1 = [str(i) for i in l1]
    l2 = [ch for ch in s.split()]
    r2 = ''.join([str(l2.index(i)) for i in l2])
    # print(l1, l2)
    return r1==r2

def wordPattern2(self, pattern: str, s: str) -> bool:

    return list(map(pattern.index, pattern))==list(map(s.index, s))


a = wordPattern("abba", "dog cat cat dog")
print(a)
