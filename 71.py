def simplifyPath( path: str) -> str:
    def deleteLast(lyst: list)-> list:
        if len(lyst)==0:
            return lyst
        s = ''.join(lyst)
        index = s.rfind('/')
        return lyst[:index+1]

    stack = []

    hasDot = False
    for ch in path:
        if ch.isalpha():
            stack.append(ch)
            hasDot = False
        elif ch is '/':
            if len(stack)>0 and stack[-1].isalpha() or len(stack)==0:
                stack.append(ch)

            hasDot = False
        elif ch is '.':
            if not hasDot:
                hasDot = True
            else:
                # last ch is '.', so it's a '..',
                # we should search up
                if len(stack)==1 and stack[0]=='/':
                    continue
                elif len(stack)>0 and stack[-1]=='/':
                    stack.pop()

                stack = deleteLast(stack)
    if len(stack)>1 and stack[-1]=='/':
        stack.pop()

    return ''.join(stack)
