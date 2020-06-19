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
    还有一个相当笨的方法就是，先把不是 alnum 的字符先过滤掉再用双指针
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
