class Solution:
    import math

    def countOdds(self, low: int, high: int) -> int:
  
        ans = math.ceil((high - low)  / 2)

        if low % 2 != 0 and high %2 != 0:
            ans += 1
        
        return ans