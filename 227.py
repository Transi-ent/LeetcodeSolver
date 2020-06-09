class Solution:
    """
    先按照顺序处理乘除运算，在依序处理加减运算
    """
    def calculate(self, s: str) -> int:
        oprt = {"+", "-", "*", "/"}
        lyst = []
        left, right = 0, 0# 用于记录数字字符串的左右索引
        while right<len(s):
            if not s[right] in oprt:# 如果s[right]不是运算符（说明是数字）
                right += 1
                if right==len(s):
                    lyst.append(int(s[left: right]))

            else:# s[right] 是运算符
                lyst.append(int(s[left: right]))
                lyst.append(s[right])
                left = right = right + 1

        left = 0 # 处理第二级运算
        print(lyst)
        while left<len(lyst):
            if lyst[left]=='*' or lyst[left]=='/':
                opr = lyst.pop(left)
                num2 = lyst.pop(left)
                num1 = lyst.pop(left-1)
                if opr=='*':
                    lyst.insert(left-1, num1*num2)
                else:
                    lyst.insert(left - 1, num1 // num2)
            else:
                left += 1
        # 处理第一级运算
        res = lyst.pop(0)
        while lyst:
            opr = lyst.pop(0)
            n2 = lyst.pop(0)
            if opr == "+":
                res += n2
            else:
                res -= n2
        return res

class Solution2:
    """
    先按照顺序处理乘除运算，在依序处理加减运算
    """
    def calculate(self, s: str) -> int:
        lyst = []
        dic = { # 字典里面根据操作符存储了函数，只进行第二级运算
            "+": lambda e: lyst.append(e),
            "-": lambda e: lyst.append(-e),
            "*": lambda e: lyst.append(lyst.pop()*e),
            "/": lambda e: lyst.append(lyst.pop()//e) if lyst[-1]>0 or lyst[-1]%e==0 else lyst.append((lyst.pop()//e)+1)
        }
        num = 0
        opr = "+"
        for ch in s+"+":# 在原字符串的后面拼接一个"+"号，是为了将最后得到的数字放进列表中
            if ch.isdigit():
                num = 10*num + int(ch)
            elif ch != " ":
                dic[opr](num)
                opr = ch
                num = 0
        return sum(lyst)


res = Solution2().calculate("14-3/2")
print(res)




