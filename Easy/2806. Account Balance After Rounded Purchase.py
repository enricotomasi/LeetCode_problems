
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        ans = 100 - purchaseAmount
        rem = purchaseAmount % 10

        if rem >= 5:
            ans -= 10 - rem
        elif rem < 5 and rem > 0:
            ans += rem
        
        return ans