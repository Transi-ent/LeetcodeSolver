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
