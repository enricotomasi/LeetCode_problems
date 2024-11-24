class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0

        weeks = n // 7
        carry = n % 7

        add = 28

        for i in range(weeks):
            ans += add
            add += 7
        
        if carry > 0:
            for i in range(carry):
                weeks += 1
                ans += weeks
        
        return ans
        