class Solution:
    def canAliceWin(self, n: int) -> bool:
        ans = False
        temp = 10
        tot = 0

        for i in range(10):
            tot += temp
            if tot > n:
                return ans
            
            temp -= 1
            ans = not ans


        return True