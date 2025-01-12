class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        m = min(a, b)
        
        ans = 1
        
        for i in range(2, m + 1):
            if a % i == 0 and b % i == 0:
                ans += 1
        
        return ans
        