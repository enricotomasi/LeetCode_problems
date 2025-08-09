class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = False

        if n < 0:
            n *= -1
            neg = True
        
        ans  = 1

        while n > 0:
            if n % 2 == 1:
                ans *= x
            x *= x
            n //= 2
        
        if neg:
            return 1 / ans
        
        return ans
        