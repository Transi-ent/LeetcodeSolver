class Solution:
    """
    使用一个栈：
    1）每当遇到一个数字，判断数字暂存区是否为0，更新暂存区数字；
    2）每遇到一个 "["，将暂存区数字压入栈；
    3）每遇到一个字母，判断暂存区字符串是否为空，进行更新；
    4）每遇到一个 "]"，从栈中进行两次 pop 操作，更新结果
    """
    def decodeString(self, s: str) -> str:
        res = ''
        stagCh = ''
        num = 0
        stack = []
        for ch in s:
            if ch.isnumeric():
                num = 10 * num + int(ch)
                if stagCh:
                    stack.append(stagCh)
                    stagCh = ''
            elif ch=='[':
                stack.append(num)
                num = 0
                stagCh = ''
            elif ch.isalpha():

                stagCh += ch
            elif ch == ']':
                if stagCh:
                    stack.append(stagCh)
                    stagCh = ''
                alpha = stack.pop()
                times = stack.pop()
                print("alpha:{}, times:{}".format(alpha, times))
                if stack:
                    print(stack)
                    print("res:{}, stack:{}".format(res, stack))
                    if isinstance(times, int):

                        if isinstance(stack[-1], str):
                            preStr = stack.pop()
                            stack.append(preStr + alpha*times)
                        else:
                            stack.append( alpha*times )
                    elif times.isalpha():
                        stack.append(times+alpha)
                else:
                    res += alpha * times
        print("res:{}, stack:{}".format(res, stack))
        if stack:
            tmpRes = ''
            for i, ch in enumerate(stack):
                if isinstance(ch, int):
                    tmpRes = tmpRes + ch*(''.join(stack[i+1:]))
                    break
                else:
                    tmpRes += ch
            res += tmpRes
        print("stack: {}".format(stack))
        print("res: ", res )
        return res#+stagCh

inp = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
Solution().decodeString(inp)
