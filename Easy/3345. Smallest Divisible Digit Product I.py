def dp(n):
    ans = 1

    while n > 0:
        ans *= n % 10
        n //= 10
    
    return ans

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            if dp(n) % t == 0:
                return n
            n += 1
        