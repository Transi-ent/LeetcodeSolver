class Solution:
    """
    A : <=1 and ...

    """
    def checkRecord(self, s: str) -> bool:
        n_A = 0
        prev = None
        L_times = 0
        for ch in s:
            if ch == 'L':
                L_times += 1
                prev = 'L'
                if L_times>2:
                    return False
            else:
                prev = ch
                L_times = 0
                if ch == "A":
                    n_A += 1

                    if n_A>1:
                        return False
        return True

