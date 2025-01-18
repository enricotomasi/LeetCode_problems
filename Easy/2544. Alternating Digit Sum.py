import math
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        pos = False

        if int(log10(n)) % 2 == 0:
            pos = True

        ans = 0

        while n > 0:
            if pos:
                ans += n % 10
            else:
                ans -= n % 10
            pos = not pos
            n //= 10
        
        return ans
        