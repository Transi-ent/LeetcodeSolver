class Solution1:
    """
    先将数组转化为整型数字，数字相加后转回list
    """
    def addToArrayForm(self, A: list, K: int) -> list:
        num = int(''.join([str(i) for i in A]))
        return [int(i) for i in str(num+K)]
