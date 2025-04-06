class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = 0
        temp = 0

        while n > 0:
            ans += pow(2, temp)
            temp += 1
            n //= 2
        
        return ans
        