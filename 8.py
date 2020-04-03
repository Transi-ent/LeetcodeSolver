class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s or s[0].isalpha():
            return 0
        s = ( s.split(' ')[0] )
        if (s.startswith('-') or s.startswith('+')):
            if len(s)==1 or not s[1].isnumeric():
                return 0
        if '.' in s:
            s = s.split('.')[0]
        if not s or s[0].isalpha():
            return 0
        for i in range(len(s)):
            if i==0:
                if s[0] in {'-', '+'} or s[0].isnumeric():
                    continue
                else:
                    return 0
            else:
                print("s:{}, i:{}".format(s, i))
                if not s[i].isnumeric():
                    s = s[:i]
                    break
        res = int(s)
        # 取值范围越界
        if res<-2**31:
            return -2**31
        elif res>2**31-1:
            return 2**31-1
        else:
            return res

res = Solution().myAtoi("  -0012a42")
print(res)
