class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        copy = num

        while copy > 0:
            digit = copy % 10
            
            if num % digit == 0:
                ans += 1
            
            copy //= 10
        
        return ans
        
