class Solution:
    def isOneBitCharacter(self, bits: list) -> bool:
        def find(index: int):
            if index >= len(bits):
                return False
            if index == len(bits)-1:
                return True

            flag = True
            if bits[index]==0:
                flag = flag and find(index+1)
            elif bits[index]==1:
                flag = flag and find(index+2)
            return flag

        return find(0)

print(Solution().isOneBitCharacter([1, 1,1,0]))


