class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left<right:
            lch, rch = s[left], s[right]
            if lch.isalnum() and rch.isalnum():
                if lch.lower() != rch.lower():
                    return False
                left+=1
                right-=1
            elif not lch.isalnum():
                left+=1
            else:
                right-=1

        return True

class Solution2:
    """
    TODO: 对字符串中的数字使用 lower() 函数竟然不报错；
    评论区方法：对s.lower() 使用filter过滤，再进行join()
    """
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left<right:
            # 先移动指针排除非字母和数字字符的情况
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            # 当两个指针所指的2个字符：1、不是同一类型；2、都是数字但不相等；3、都是字母但不相等
            if s[left].isdigit()!=s[right].isdigit() or\
                    (s[left].isdigit() and s[left]!=s[right]) or\
                    (s[left].isalpha())and s[left].lower()!=s[right].lower():
                return False
            left += 1
            right -= 1
        return True

print(Solution2().isPalindrome("race a car"))
