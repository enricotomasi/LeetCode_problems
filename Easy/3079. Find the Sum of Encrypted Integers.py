def enc(n):
    digits = 0
    maxdigit = -1

    while n > 0:
        digits += 1
        
        digit = n % 10
        maxdigit = max(maxdigit, digit)
        
        n //= 10
    
    ans = 0
    
    for i in range(digits):
        ans += maxdigit * pow(10, i)

    return ans
    

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        
        for it in nums:
            ans += enc(it)
        
        return ans