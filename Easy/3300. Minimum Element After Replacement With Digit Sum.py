import sys

def ds(n):
    ans = 0
    
    while n > 0:
        ans += n % 10
        n //= 10

    return ans

class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = sys.maxsize

        for it in nums:
            ans = min(ans, ds(it))

        return ans