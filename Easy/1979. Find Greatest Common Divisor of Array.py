import sys
import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        ma = sys.maxsize * -1
        mi = sys.maxsize

        for it in nums:
            ma = max(ma, it)
            mi = min(mi, it)
        
        # print(f"Max: {ma} min: {mi}")

        return math.gcd(ma, mi)
        