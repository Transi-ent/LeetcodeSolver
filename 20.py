def isValid(s: str) -> bool:

    lyst = []

    for ch in s:
        if ch in {'(', '[', '{'}:
            lyst.append(ch)
        else:
            if len(lyst)==0:
                return 0
            if ch==')':
                left = lyst.pop()
                if left != '(':
                    return False
            elif ch==']':
                left = lyst.pop()
                if left != '[':
                    return False
            elif ch=='}':
                left = lyst.pop()
                if left != '{':
                    return False

    return len(lyst)==0


