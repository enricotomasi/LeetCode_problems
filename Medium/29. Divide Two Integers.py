class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == divisor:
            return 1
        
        if divisor == 1:
            return dividend

        if dividend == pow(-2, 31) and divisor == -1:
            return pow(2, 31) - 1
        
        neg = False

        if divisor < 0 and dividend >= 0 or divisor >= 0 and dividend < 0:
            neg = True
        
        if dividend < 0:
            dividend *= -1
        
        if divisor < 0:
            divisor *= -1
       
        ans = 0 

        while dividend >= divisor:
            temp = divisor
            count = 1

            while temp * 2 <= dividend:
                temp *= 2
                count *= 2
            
            ans += count
            dividend -= temp
        

        if not neg:
            return min(ans, pow(2, 31) - 1)
        else:
            return max((ans * - 1), pow(-2, 31))
        
        