class Solution:
    def reverse(self, x: int) -> int:
        neg = False

        if x < 1:
            neg = True
            x *= -1
        
        s = str(x)
        s = s[ : : -1 ]


        ans = int(s)
        
        if neg:
            ans *= -1
        
        if ans < pow(-2, 31) or ans > pow(2, 31) - 1:
            return 0
        
        return ans