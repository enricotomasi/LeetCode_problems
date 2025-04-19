import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1

        for i in range(n):
            for j in range(i, n):
                temp = nums[ i : j + 1 ]

                mcd = reduce(math.gcd, temp)
                mcm = reduce(math.lcm, temp)

                product = math.prod(temp)
                
                if product == mcd * mcm:
                    ans = max(len(temp), ans)
        
        return ans
        
