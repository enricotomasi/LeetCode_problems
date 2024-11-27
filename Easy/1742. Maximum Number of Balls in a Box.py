def digitCount(n):
    ans = 0

    while n > 0:
        ans += n % 10
        n //= 10
    
    return ans

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = dict()

        for i in range(lowLimit, highLimit + 1):
            digits = digitCount(i)

            if digits in d:
                d[digits] += 1
            else:
                d[digits] = 1
        
        ans = 0

        for it in d:
            ans = max(ans, d[it])
        
        return ans
