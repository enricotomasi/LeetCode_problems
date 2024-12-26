def digev(n):
    sum = 0

    while n > 0:
        sum += n % 10
        n //= 10
    
    return sum % 2 == 0


class Solution:
    def countEven(self, num: int) -> int:
        ans = 0

        for i in range(1, num + 1):
            if digev(i):
                ans += 1
        
        return ans
        