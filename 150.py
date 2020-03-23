def evalRPN( tokens: list) -> int:
    """
    1, construct a new list to store numbers;
    2, once encounter a operator, get 2 num from list;
    3, after operation, push the result back to the list;
    :param tokens:
    :return:
    """
    nums = []

    for em in tokens:
        if em.isnumeric():
            nums.append(int(em))
        elif len(em)>1:
            nums.append(int(em))
        else:
            # em is a operator, we need 2 nums
            print(nums)
            first = nums.pop()
            second = nums.pop()
            #res = None
            if em=='+':
                res = first + second
                print('+')
            elif em=='-':
                res = second - first
                print('-')
            elif em=='*':
                res = second * first
                print('*')
            else:
                res = second // first
                if first*second<0 and second/first!=second//first:
                    res += 1
                print('/')

            nums.append(res)

    return nums.pop()

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
